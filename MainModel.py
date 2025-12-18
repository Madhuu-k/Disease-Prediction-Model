import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv(r"C:\Users\MADHU\Desktop\Projects\Disease Prediction Model\Datasets\Training.csv")

target = "prognosis"
x = data.drop(columns=[target]).values
y = data[target].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(
    n_estimators=200,
    n_jobs=1,
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