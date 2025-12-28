import pandas as pd

DATASET_PATH = r"C:\Users\MADHU\Desktop\Projects\Disease Prediction Model\Datasets\Training.csv"
df = pd.read_csv(DATASET_PATH)

TARGET = "prognosis"
SYMPTOM = [c for c in df.columns if c != TARGET]

def explain_prediction(disease_name, ml_features, top_n=5):
    disease_rows = df[df[TARGET] == disease_name]

    active_features = [k for k, v in ml_features.items() if v == 1]

    if not active_features:
        return []

    freq = disease_rows[active_features].mean().sort_values(ascending=False)

    return freq.head(top_n).index.tolist()
