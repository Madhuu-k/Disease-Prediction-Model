import numpy as np
import joblib
import preprocess

model = joblib.load("models/disease_model.pkl")

def predict_disease(data):
    features = preprocess(data)
    proba = model.predict_proba(features)[0][1]
    
    return {
        "risk" : "High" if proba > 0.6 else "Low",
        "probability": round(float(proba), 3)
    }