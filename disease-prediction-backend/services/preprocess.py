import numpy as np

MODEL_FEATURE_ORDER = []

def preprocess(data):
    feature_vector = []
    
    for feature in MODEL_FEATURE_ORDER:
        value = data.get(feature, 0)
        if value in ("", None):
            value = 0
        feature_vector.append(float(value))
        
    return np.array(feature_vector).reshape(1, -1)
        
        
    