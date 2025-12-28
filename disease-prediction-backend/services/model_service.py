import joblib 
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

ROUTING_MODEL_PATH = os.path.join(MODEL_DIR, "routing_model.pkl")
PHASE1_FEATURES_PATH = os.path.join(MODEL_DIR, "phase1_features.pkl")
PHASE2_GROUPS_PATH = os.path.join(MODEL_DIR, "phase2_groups.pkl")

routing_model = joblib.load(ROUTING_MODEL_PATH)
ML_ROUTING_FEATURES = joblib.load(PHASE1_FEATURES_PATH)
PHASE2_GROUPS = joblib.load(PHASE2_GROUPS_PATH)

def get_phase2_groups(ml_feature_dict: dict, threshold: float = 0.5):
     # Ensure correct feature order
    df = pd.DataFrame([ml_feature_dict])[ML_ROUTING_FEATURES]

    # Predict probabilities for each group
    probs = routing_model.predict_proba(df)

    selected_groups = []

    for i, group in enumerate(PHASE2_GROUPS):
        # probs[i][0][1] -> probability of class 1 for group i
        if probs[i][0][1] >= threshold:
            selected_groups.append(group)

    return selected_groups