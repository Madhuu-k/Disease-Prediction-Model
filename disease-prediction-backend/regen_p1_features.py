# regenerate_phase1_features.py
import joblib
from data.question_bank import PHASE_1_QUESTIONS

phase1_features = list(PHASE_1_QUESTIONS.keys())

joblib.dump(phase1_features, "models/phase1_features.pkl")

print("Regenerated phase1_features.pkl:")
print(phase1_features)
