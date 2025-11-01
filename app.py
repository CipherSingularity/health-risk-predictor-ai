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

        # Map form data
        input_data = {
            'Age': int(data['age']),
            'Gender': 1 if data['gender'] == 'male' else 0,
            'Glucose': float(data['glucose']),
            'HbA1c': float(data['hba1c']),
            'Systolic': int(data['systolic']),
            'Diastolic': int(data['diastolic']),
            'BMI': float(data['bmi']),
            'Cholesterol': float(data['cholesterol']),
            'Triglycerides': float(data['triglycerides']),
            'Smoking': 1 if data['smoking'] == 'yes' else 0,
            'Alcohol': 1 if data['alcohol'] in ['occasional', 'regular'] else 0,
            'Physical_Activity': {'low':0, 'moderate':1, 'high':2}[data['activity']],
            'Diet_Score': int(data['diet_score']),
            'Family_History': 1 if data['family_history'] == 'yes' else 0,
            'Sleep_Hours': float(data['sleep']),
            'Stress_Level': {'low':0, 'moderate':1, 'high':2}[data['stress']],
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
    app.run(debug=True)