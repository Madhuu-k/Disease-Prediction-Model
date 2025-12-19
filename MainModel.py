import numpy as np
import warnings
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
warnings.filterwarnings("ignore", category=UserWarning)

train_df = pd.read_csv(r"C:\Users\MADHU\Desktop\Projects\Disease Prediction Model\Datasets\Training.csv")
test_df = pd.read_csv(r"C:\Users\MADHU\Desktop\Projects\Disease Prediction Model\Datasets\Testing.csv")

train_df = train_df.drop(columns=["Unnamed: 133"], errors="ignore")
test_df = test_df.drop(columns=["Unnamed: 133"], errors="ignore")

user_input_phase1 = {
    "fever": 1,
    "fatigue": 1,
    "headache": 1,
    "vomiting": 1,
    "cough": 0,
    "breathlessness": 0
}


x_train = train_df.drop("prognosis", axis=1)
y_train = train_df["prognosis"]

x_test = test_df.drop("prognosis", axis=1)
y_test = test_df["prognosis"]

all_features = x_train.columns.tolist()

rf = RandomForestClassifier(
    n_estimators=200,
    n_jobs= -1,
    max_depth=6,
    random_state=42,
    class_weight="balanced",
    min_samples_leaf=2
)
rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)
print("Predictions: ", y_pred[:5])
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
print("Classification Report: ", classification_report(y_test, y_pred))

importance = pd.Series(
    rf.feature_importances_,
    index=x_train.columns
).sort_values(ascending=False)

print("Top 15 Symptoms influcencing prediction: ")
print(importance.head(10))

def build_input_vector(user_input, all_features):
    input_vector = {feature: 0 for feature in all_features}
    for symptom, value in user_input.items():
        if symptom in input_vector:
            input_vector[symptom] = value
    return pd.DataFrame([input_vector])

    
def get_discriminative_symptomps(df, diseases, top_k=5):
    subset = df[df["prognosis"].isin(diseases)]
    symptom_cols = df.columns.drop("prognosis")
    
    means = subset.groupby("prognosis")[symptom_cols].mean()
    varinace = means.var(axis=0)
    
    return varinace.sort_values(ascending=False).head(top_k).index.tolist()


def diagnose_phase1_phase2(
    rf, 
    train_df, 
    all_features, 
    phase1_input, 
    top_n=3, 
    phase2_k=5
):
    x_user_phase1 = build_input_vector(phase1_input, all_features)
    probas = rf.predict_proba(x_user_phase1)[0]
    classes = rf.classes_
    
    results = sorted(
        zip(classes, probas),
        key=lambda x : x[1],
        reverse=True
    )
    
    top_disease = [d for d, _ in results[:top_n]]
    
    phase2_symptoms = get_discriminative_symptomps(
        train_df,
        top_disease,
        top_k=phase2_k
    )
    
    return {
        "phase1_candidates": results[:top_n],
        "ask_next": phase2_symptoms
    }