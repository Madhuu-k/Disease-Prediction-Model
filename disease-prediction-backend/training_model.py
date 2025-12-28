import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import joblib

data = pd.read_csv(r"C:\Users\MADHU\Desktop\Projects\Disease Prediction Model\Datasets\Training.csv")