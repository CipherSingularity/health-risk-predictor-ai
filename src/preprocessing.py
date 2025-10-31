# src/preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    
    # Drop junk
    df = df.drop(['random_notes', 'noise_col', 'LengthOfStay'], axis=1, errors='ignore')
    
    # Split BP
    if 'Blood_Pressure' in df.columns:
        bp = df['Blood_Pressure'].str.split('/', expand=True).astype(float)
        df['Systolic'] = bp[0]
        df['Diastolic'] = bp[1]
        df = df.drop('Blood_Pressure', axis=1)
    
    # Encode categoricals
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df['Smoking'] = df['Smoking'].map({'Yes': 1, 'No': 0, 'Former': 1}).fillna(0)
    df['Alcohol'] = df['Alcohol'].map({'Yes': 1, 'No': 0, 'Occasional': 1, 'Regular': 1}).fillna(0)
    df['Family_History'] = df['Family_History'].map({'Yes': 1, 'No': 0})
    
    # Activity & Stress ordinal
    activity_map = {'Low': 0, 'Moderate': 1, 'High': 2}
    stress_map = {'Low': 0, 'Moderate': 1, 'High': 2}
    df['Physical_Activity'] = df['Physical_Activity'].map(activity_map)
    df['Stress_Level'] = df['Stress_Level'].map(stress_map)
    
    # Fill NA
    for col in df.select_dtypes(include=['float64', 'int64']):
        df[col].fillna(df[col].median(), inplace=True)
    for col in df.select_dtypes(include=['object']):
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def create_features(df):
    df = df.copy()
    if 'Cholesterol' in df.columns and 'HDL' not in df.columns:
        df['HDL'] = df['Cholesterol'] * 0.25  # placeholder
    df['TC_HDL_Ratio'] = df['Cholesterol'] / df['HDL']
    df['BMI_Category'] = pd.cut(df['BMI'], bins=[0, 18.5, 25, 30, 100], labels=[0,1,2,3])
    return df

def get_preprocessor():
    return joblib.load('models/scaler.pkl') if os.path.exists('models/scaler.pkl') else None