import requests
sample = {
    'age': '55', 'gender': 'male', 'glucose': '135', 'hba1c': '6.3',
    'systolic': '145', 'diastolic': '92', 'bmi': '32', 'cholesterol': '245',
    'triglycerides': '180', 'smoking': 'yes', 'alcohol': 'no',
    'activity': 'low', 'diet_score': '45', 'family_history': 'yes',
    'sleep': '5', 'stress': 'high'
}
resp = requests.post('http://127.0.0.1:5000/predict', json=sample, timeout=10)
print('Status', resp.status_code)
print(resp.text)
