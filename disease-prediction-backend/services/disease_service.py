import os
import joblib
import pandas as pd

# LOAD ARTIFACTS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

DISEASE_MODEL_PATH = os.path.join(MODEL_DIR, "disease_model.pkl")
FEATURES_PATH = os.path.join(MODEL_DIR, "all_features.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

disease_model = joblib.load(DISEASE_MODEL_PATH)
ALL_FEATURES = joblib.load(FEATURES_PATH)
label_encoder = joblib.load(ENCODER_PATH)



def predict_disease(ml_feature_dict: dict, top_k: int = 3):

    # Initialize full feature vector with zeros
    full_features = {feature: 0 for feature in ALL_FEATURES}

    # Fill inferred features
    for key, value in ml_feature_dict.items():
        if key in full_features:
            full_features[key] = value

    # Convert to DataFrame (correct order)
    df = pd.DataFrame([full_features])[ALL_FEATURES]

    # Predict probabilities
    probs = disease_model.predict_proba(df)[0]

    # Get top-K indices
    top_indices = probs.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "disease": label_encoder.inverse_transform([idx])[0],
            "confidence": round(float(probs[idx]), 3)
        })

    return results