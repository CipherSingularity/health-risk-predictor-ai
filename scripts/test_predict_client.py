import sys
from pathlib import Path
# Ensure repo root is on path and import local app module
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
from app import app
import json

sample = {
    'age': '55', 'gender': 'male', 'glucose': '135', 'hba1c': '6.3',
    'systolic': '145', 'diastolic': '92', 'bmi': '32', 'cholesterol': '245',
    'triglycerides': '180', 'smoking': 'yes', 'alcohol': 'no',
    'activity': 'low', 'diet_score': '45', 'family_history': 'yes',
    'sleep': '5', 'stress': 'high'
}

with app.test_client() as client:
    resp = client.post('/predict', json=sample)
    print('Status code:', resp.status_code)
    try:
        print('JSON:', resp.get_json())
    except Exception as e:
        print('Response data:', resp.data)
