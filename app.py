# app.py
from flask import Flask, render_template, request, jsonify
from src.prediction import predict_risk
from src.recommendations import get_recommendations
# from src.explainer import get_shap_explanation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        app.logger.info('Incoming /predict JSON: %s', data)
        # Basic validation: ensure JSON payload and required fields exist
        if not data or not isinstance(data, dict):
            return jsonify({'error': 'Request must be JSON with form fields'}), 400
        required = ['age','gender','glucose','hba1c','systolic','diastolic','bmi','cholesterol','triglycerides','smoking','alcohol','activity','diet_score','family_history','sleep','stress']
        missing = [k for k in required if k not in data or data.get(k) in (None, '')]
        if missing:
            return jsonify({'error': 'Missing required fields', 'missing': missing}), 400
        # Map form data
        # Pass categorical strings so the preprocessor's OneHotEncoder can match categories
        input_data = {
            'Age': int(data['age']),
            'Gender': data['gender'],
            'Glucose': float(data['glucose']),
            'HbA1c': float(data['hba1c']),
            'Systolic': int(data['systolic']),
            'Diastolic': int(data['diastolic']),
            'BMI': float(data['bmi']),
            'Cholesterol': float(data['cholesterol']),
            'Triglycerides': float(data['triglycerides']),
            'Smoking': data['smoking'],
            'Alcohol': data['alcohol'],
            'Physical_Activity': data['activity'],
            'Diet_Score': int(data['diet_score']),
            'Family_History': data['family_history'],
            'Sleep_Hours': float(data['sleep']),
            'Stress_Level': data['stress'],
            'TC_HDL_Ratio': 0  # placeholder
        }

        risks = predict_risk(input_data)
        recs = get_recommendations(risks, input_data)
        app.logger.info('Predicted risks: %s, recommendations: %s', risks, recs)

        return jsonify({
            'risks': risks,
            'recommendations': recs
            # 'shap_plot': get_shap_explanation(input_data)
        })
    except Exception as e:
        # Provide detailed error information in debug mode so the front-end can show it
        import traceback
        tb = traceback.format_exc()
        app.logger.exception('Error in /predict')
        return jsonify({'error': str(e), 'traceback': tb}), 500

if __name__ == '__main__':
    # Disable the auto-reloader/watchdog to avoid intermittent restarts while loading model artifacts
    app.run(debug=True, use_reloader=False)