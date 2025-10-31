import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt
import io
import base64

def get_shap_explanation(input_dict, disease='diabetes'):
    model = joblib.load(f'models/{disease}_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    
    df = pd.DataFrame([input_dict])
    df = df.reindex(columns=[...], fill_value=0)  # same as prediction.py
    X = scaler.transform(df)
    
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    
    plt.figure(figsize=(8, 6))
    shap.force_plot(explainer.expected_value, shap_values[0], df.iloc[0], matplotlib=True, show=False)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode()
    plt.close()
    return f"data:image/png;base64,{img_base64}"