# src/model_training.py
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os
from preprocessing import load_and_clean_data, create_features

DATA_PATH = "data/raw/sample_data.csv"
MODELS_DIR = "models"

os.makedirs(MODELS_DIR, exist_ok=True)

# Load & clean
df = load_and_clean_data(DATA_PATH)
df = create_features(df)

# Define targets
df['diabetes'] = ((df['Glucose'] > 126) | (df['HbA1c'] > 6.5)).astype(int)
df['heart_disease'] = ((df['Systolic'] >= 140) | (df['Cholesterol'] > 240) | (df['Smoking'] == 1)).astype(int)
df['stroke'] = ((df['Systolic'] >= 160) | (df['Age'] > 65)).astype(int)  # simplified

# Features
feature_cols = ['Age','Gender','Glucose','HbA1c','Systolic','Diastolic','BMI','Cholesterol',
                'Triglycerides','Smoking','Alcohol','Physical_Activity','Diet_Score',
                'Family_History','Sleep_Hours','Stress_Level','TC_HDL_Ratio']

X = df[feature_cols]
y_diabetes = df['diabetes']
y_heart = df['heart_disease']
y_stroke = df['stroke']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, f'{MODELS_DIR}/scaler.pkl')

# Train-test split
X_train, X_test = train_test_split(X_scaled, test_size=0.2, random_state=42)

# Train models
models = {}
targets = {'diabetes': y_diabetes, 'heart_disease': y_heart, 'stroke': y_stroke}

for name, y in targets.items():
    y_train = y.iloc[X_train.index]
    model = xgb.XGBClassifier(n_estimators=200, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    models[name] = model
    joblib.dump(model, f'{MODELS_DIR}/{name}_model.pkl')

print("All models trained and saved!")