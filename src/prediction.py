# src/prediction.py
import joblib
import pandas as pd

def predict_risk(input_dict):
    scaler = joblib.load('models/scaler.pkl')
    models = {
        'diabetes': joblib.load('models/diabetes_model.pkl'),
        'heart_disease': joblib.load('models/heart_disease_model.pkl'),
        'stroke': joblib.load('models/stroke_model.pkl')
    }
    
    df = pd.DataFrame([input_dict])
    df = df.reindex(columns=[
        'Age','Gender','Glucose','HbA1c','Systolic','Diastolic','BMI','Cholesterol',
        'Triglycerides','Smoking','Alcohol','Physical_Activity','Diet_Score',
        'Family_History','Sleep_Hours','Stress_Level','TC_HDL_Ratio'
    ], fill_value=0)
    
    df['TC_HDL_Ratio'] = df['Cholesterol'] / 50  # fallback
    
    X = scaler.transform(df)
    
    results = {}
    for name, model in models.items():
        proba = model.predict_proba(X)[0][1]
        results[name] = round(proba * 100, 1)
    
    return results