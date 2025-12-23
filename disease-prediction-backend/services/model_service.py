import numpy as np
import joblib
import pandas as pd

phase1_features = joblib.load("models/phase1_features.pkl")
phase2_groups = joblib.load("models/phase2_groups.pkl")
routing_model = joblib.load("models/routing_model.pkl")

def get_phase2_features(input_json, threshold=0.5):
    user_df = pd.DataFrame([{
        feature: input_json.get(feature, 0)
        for feature in phase1_features
    }])
    
    probs = routing_model.predict_proba(user_df)
    
    selected_groups = []
    for i, group_name in enumerate(phase2_groups.keys()):
        if probs[i][0][1] >= threshold:
            selected_groups.append(group_name)

    return selected_groups
    