# train_disease_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# -----------------------
# Load dataset
# -----------------------
df = pd.read_csv("Datasets/Training.csv")

TARGET = "prognosis"
FEATURES = [c for c in df.columns if c != TARGET]

X = df[FEATURES]
y = df[TARGET]

# Encode target
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

model.fit(X, y_encoded)

# Save artifacts
joblib.dump(model, "disease_model.pkl")
joblib.dump(FEATURES, "all_features.pkl")
joblib.dump(le, "label_encoder.pkl")

print("✅ Disease model trained and saved")
