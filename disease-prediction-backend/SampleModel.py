import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import joblib

data = pd.read_csv(r"C:\Users\MADHU\Desktop\Projects\Disease Prediction Model\Datasets\Training.csv")

TARGET = "prognosis"
FEATURES = [c for c in data.columns if c != TARGET]

symptom_frequency = data[FEATURES].mean().sort_values(ascending=False)

# ----------------------- PHASE 1 CANDIDATES ---------------------- #
p1_candidates = symptom_frequency[(symptom_frequency > 0.15) & (symptom_frequency < 0.6)]

PHASE1_FEATURES = p1_candidates.head(15).index.tolist()

# ----------------------- PHASE 2 CANDIDATES ---------------------- #
p2_candidates = symptom_frequency[symptom_frequency <= 0.15]
corr = data[p2_candidates.index].corr().fillna(0)

clustering = AgglomerativeClustering(
    n_clusters=5,
    metric="euclidean",
    linkage="ward"
)

labels = clustering.fit_predict(corr)
PHASE2_GROUPS = {}

for symptom, label in zip(corr.columns, labels):
    PHASE2_GROUPS.setdefault(f"group_{label}", []).append(symptom)
    
PHASE2_GROUPS = {
    k: v for k, v in PHASE2_GROUPS.items() if len(v) >= 5
}

# -------------- BUILD VALID ROUTING FROM PHASE 1 TO PHASE 2 ----------------- #

def build_routing_labels(df, groups):
    labels = {}
    
    for group, features in groups.items():
        valid_feats = [f for f in features if f in df.columns]
        labels[group] = (df[valid_feats].sum(axis=1) > 0).astype(int)
        
    return pd.DataFrame(labels)

y_routing = build_routing_labels(data, PHASE2_GROUPS)
x_phase1 = data[PHASE1_FEATURES]

# ----------------------------- TRAIN AND TEST THE MODEL ---------------------------------#

x_train, x_test, y_train, y_test = train_test_split(x_phase1, y_routing, random_state=42, test_size=0.2)

routing_model = MultiOutputClassifier(
    RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42,
        class_weight="balanced"
    )
)

routing_model.fit(x_train, y_train)

y_pred = routing_model.predict(x_test)

for i, col in enumerate(y_routing.columns):
    print(f"\nRouting performance for {col.upper()}:")
    print(classification_report(y_test[col], y_pred[:, i]))
    
def get_groups(user_phase1_df, threshold=0.5):
    probs = routing_model.predict_proba(user_phase1_df)
    selected = []
    
    for i, group in enumerate(y_routing.columns):
        if probs[i][0][1] >= threshold:
            selected.append(group)
    
    return selected

print(PHASE1_FEATURES)

joblib.dump(routing_model, "routing_model.pkl")
joblib.dump(PHASE1_FEATURES, "phase1_features.pkl")
joblib.dump(PHASE2_GROUPS, "phase2_groups.pkl")