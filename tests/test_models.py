import sys
import os
from pathlib import Path

# Ensure repo root/src is on sys.path regardless of current working directory
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = REPO_ROOT / 'src'
sys.path.insert(0, str(SRC_PATH))

from prediction import predict_risk

def test_prediction():
    sample = {
        'Age': 55, 'Gender': 1, 'Glucose': 135, 'HbA1c': 6.3,
        'Systolic': 145, 'Diastolic': 92, 'BMI': 32, 'Cholesterol': 245,
        'Triglycerides': 180, 'Smoking': 1, 'Alcohol': 0,
        'Physical_Activity': 0, 'Diet_Score': 45, 'Family_History': 1,
        'Sleep_Hours': 5, 'Stress_Level': 2, 'TC_HDL_Ratio': 5
    }
    risks = predict_risk(sample)
    assert all(k in risks for k in ['diabetes', 'heart_disease', 'stroke'])
    print("Test passed!")