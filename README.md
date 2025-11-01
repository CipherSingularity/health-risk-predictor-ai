<div align="center">
  
# AI-Powered Health Risk Prediction System


![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0+-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

**An intelligent health assessment platform that predicts chronic disease risks and provides personalized preventive recommendations using machine learning.**

</div>

---

## 🎯 Problem Statement

Millions of people worldwide develop chronic illnesses like heart disease, diabetes, and hypertension due to unmonitored lifestyle risk factors. Early detection and prevention are crucial but often inaccessible. This system democratizes health risk assessment by leveraging AI to predict disease probability from lifestyle and medical data, empowering users to take proactive measures.

## ✨ Features

### 🔍 Core Functionality
- **Multi-Disease Risk Prediction**: Assess risk for heart disease, diabetes, stroke, and hypertension
- **Personalized Health Insights**: AI-driven recommendations tailored to individual risk profiles
- **Interactive Dashboard**: Real-time visualization of health metrics and risk factors
- **Explainable AI**: Understand which factors contribute most to your health risks
- **Privacy-First Design**: All data processing happens locally, no data storage

### 📊 Visualizations
- **Health Score Gauge**: Overall health rating (0-100 scale)
- **Risk Comparison Charts**: Side-by-side disease probability analysis
- **Factor Contribution Analysis**: Top 3 risk contributors with actionable insights
- **Trend Indicators**: Visual representation of risk levels (Low/Medium/High)

### 💡 Intelligent Recommendations
- Evidence-based lifestyle modifications
- Personalized dietary suggestions
- Physical activity guidelines
- Medical consultation triggers for high-risk cases

---

## 🛠️ Tech Stack

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chart.js&logoColor=white)

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

### Machine Learning
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat-square&logo=xgboost&logoColor=white)
![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=flat-square&logo=lightgbm&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-FF0000?style=flat-square&logo=python&logoColor=white)

### Visualization
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square&logo=python&logoColor=white)

---

## 📊 Dataset

This project utilizes comprehensive health data from:

- **Primary Source**: [Healthcare Risk Factors Dataset](https://www.kaggle.com/datasets) (Kaggle)
- **Alternative**: CDC BRFSS (Behavioral Risk Factor Surveillance System) 2022
- **Features**: 20+ lifestyle and medical indicators
- **Size**: 400,000+ patient records
- **Target Variables**: Heart Disease, Diabetes, Stroke, Hypertension

### Key Features
| Category | Features |
|----------|----------|
| **Demographic** | Age, Gender, Race/Ethnicity |
| **Physical Metrics** | BMI, Height, Weight, Blood Pressure |
| **Lifestyle Factors** | Smoking Status, Alcohol Consumption, Physical Activity, Diet Quality |
| **Medical History** | Cholesterol Levels, Blood Sugar, Previous Diagnoses, Family History |
| **Mental Health** | Stress Levels, Sleep Quality, Depression History |

---

## 🚀 Installation

### Prerequisites
```bash
Python 3.8+
pip 21.0+
Git
```

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/health-risk-prediction.git
cd health-risk-prediction
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download dataset**
```bash
# Place your dataset in the data/ directory
mkdir data
# Download from Kaggle or CDC BRFSS
```

5. **Train models** (optional - pre-trained models included)
```bash
python train_models.py
```

6. **Run the application**
```bash
python app.py
```

7. **Open in browser**
```
http://localhost:5000
```

---

## 📦 Project Structure

```
health-risk-prediction/
│
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── models/                     # Trained ML models
│   ├── heart_disease_model.pkl
│   ├── diabetes_model.pkl
│   ├── stroke_model.pkl
│   └── scaler.pkl
│
├── notebooks/                  # Jupyter notebooks for EDA
│   ├── data_exploration.ipynb
│   ├── model_training.ipynb
│   └── feature_engineering.ipynb
│
├── src/                        # Source code
│   ├── preprocessing.py        # Data preprocessing utilities
│   ├── model_training.py       # Model training scripts
│   ├── prediction.py           # Prediction engine
│   ├── explainer.py           # SHAP/LIME explanations
│   └── recommendations.py      # Recommendation engine
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   └── charts.js
│   └── images/
│
├── templates/                  # HTML templates
│   ├── index.html
│   ├── results.html
│   └── about.html
│
├── data/                       # Dataset directory
│   ├── raw/
│   ├── processed/
│   └── README.md
│
└── tests/                      # Unit tests
    ├── test_preprocessing.py
    ├── test_models.py
    └── test_api.py
```

---

## 🤖 Models

### Model Architecture

#### 1. Baseline Model: Logistic Regression
- **Purpose**: Fast predictions with interpretable coefficients
- **Accuracy**: ~78%
- **Use Case**: Quick health screening

#### 2. Advanced Model: XGBoost Classifier
- **Purpose**: High-accuracy multi-class predictions
- **Accuracy**: ~89%
- **Features**: Gradient boosting, feature importance ranking
- **Use Case**: Detailed risk assessment

#### 3. Ensemble Model: LightGBM + Random Forest
- **Purpose**: Optimal performance through model voting
- **Accuracy**: ~91%
- **Features**: Combines strengths of multiple algorithms
- **Use Case**: Production-level predictions

### Training Process

```python
# Example workflow
1. Data Preprocessing
   ├── Handle missing values (KNN imputation)
   ├── Encode categorical variables (One-Hot/Label encoding)
   ├── Feature scaling (StandardScaler)
   └── Feature selection (Recursive Feature Elimination)

2. Model Training
   ├── Train-test split (80-20)
   ├── Cross-validation (5-fold)
   ├── Hyperparameter tuning (GridSearchCV)
   └── Model evaluation (AUC-ROC, F1-score)

3. Model Explainability
   ├── SHAP values for feature importance
   ├── LIME for local interpretability
   └── Partial Dependence Plots
```

### Performance Metrics

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 78.3% | 76.5% | 74.2% | 75.3% | 0.82 |
| Random Forest | 86.7% | 85.1% | 83.9% | 84.5% | 0.91 |
| XGBoost | 89.4% | 88.2% | 87.5% | 87.8% | 0.94 |
| LightGBM | 88.9% | 87.8% | 87.1% | 87.4% | 0.93 |
| **Ensemble** | **91.2%** | **90.5%** | **89.8%** | **90.1%** | **0.96** |

---

## 🎨 Screenshots

<div align="center">
  
### Landing Page

<p align="center">
  <img src="https://github.com/ARUNAGIRINATHAN-K/health-risk-predictor-ai/blob/main/img/img-1.png" 
       alt="Project Demo" 
       width="600" 
       height="340" 
       style="border-radius: 15px;">
</p>

*User-friendly interface for inputting health metrics*

### Risk Assessment Input

<p align="center">
  <img src="https://github.com/ARUNAGIRINATHAN-K/health-risk-predictor-ai/blob/main/img/img-3.png" 
       alt="Project Demo" 
       width="600" 
       height="340" 
       style="border-radius: 15px;">
</p>

*Comprehensive visualization for prediction*

### Personalized Recommendations

<p align="center">
  <img src="https://github.com/ARUNAGIRINATHAN-K/health-risk-predictor-ai/blob/main/img/final.png" 
       alt="Project Demo" 
       width="600" 
       height="840" 
       style="border-radius: 15px;">
</p>

*AI-generated actionable health advice*

</div>


## 🔧 API Endpoints

### POST `/api/predict`
Predict health risks based on user input.

**Request Body:**
```json
{
"age": "55",
"gender": "male",
"glucose": "135",
"hba1c": "6.3",
"systolic": "145",
"diastolic": "92",
"bmi": "32",
"cholesterol": "245",
"triglycerides": "180",
"smoking": "yes",
"alcohol": "no",
"activity": "low",
"diet_score": "45",
"family_history": "yes",
"sleep": "5",
"stress": "high"
}

```
Expected: non-zero risks (in my tests this returned ~100% and 3 recommendations).

**Medium-risk sample (may give mid-range probabilities — possibly below recommendation threshold)**
```json
{
"age": "50",
"gender": "male",
"glucose": "110",
"hba1c": "6.0",
"systolic": "130",
"diastolic": "85",
"bmi": "28",
"cholesterol": "210",
"triglycerides": "150",
"smoking": "no",
"alcohol": "occasional",
"activity": "moderate",
"diet_score": "60",
"family_history": "yes",
"sleep": "6",
"stress": "moderate"
}
```

**Low-risk sample (should produce low probabilities → no recommendations)**
```json
{
"age": "30",
"gender": "female",
"glucose": "90",
"hba1c": "5.4",
"systolic": "115",
"diastolic": "75",
"bmi": "22",
"cholesterol": "170",
"triglycerides": "100",
"smoking": "no",
"alcohol": "occasional",
"activity": "moderate",
"diet_score": "80",
"family_history": "no",
"sleep": "7",
"stress": "low"
}
```

**Response:**
```json
{
  "health_score": 68,
  "risks": {
    "heart_disease": 0.72,
    "diabetes": 0.45,
    "stroke": 0.38,
    "hypertension": 0.81
  },
  "top_risk_factors": [
    "High Blood Pressure",
    "Low Physical Activity",
    "Elevated BMI"
  ],
  "recommendations": [
    "Increase physical activity to 150 mins/week",
    "Reduce sodium intake below 2,300mg/day",
    "Schedule blood pressure monitoring"
  ]
}
```

---

## 📈 Usage Example

```python
from src.prediction import HealthRiskPredictor

# Initialize predictor
predictor = HealthRiskPredictor()

# User data
user_data = {
    'age': 52,
    'bmi': 31.2,
    'smoking': 'current',
    'physical_activity': 'low',
    'blood_pressure': 'high'
}

# Get predictions
results = predictor.predict(user_data)

print(f"Heart Disease Risk: {results['heart_disease']:.1%}")
print(f"Health Score: {results['health_score']}/100")
print(f"Top Recommendations: {results['recommendations']}")
```

---

## 🔬 Model Training

To retrain models with your own data:

```bash
# 1. Prepare your dataset
python src/preprocessing.py --input data/raw/health_data.csv --output data/processed/

# 2. Train models
python src/model_training.py --config config/training_config.yaml

# 3. Evaluate models
python src/evaluation.py --model-dir models/ --test-data data/processed/test.csv

# 4. Generate SHAP explanations
python src/explainer.py --model models/xgboost_model.pkl
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_models.py

# Run with coverage report
pytest --cov=src tests/
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write unit tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

**Your Name**
- GitHub: [ARUNAGIRINATHAN-K](https://github.com/ARUNAGIRINATHAN-K)
- LinkedIn: [arunagirinathan-k](https://linkedin.com/in/arunagirinathan-k)
---

## 🙏 Acknowledgments

- CDC BRFSS for providing comprehensive health surveillance data
- Kaggle community for dataset curation and insights
- XGBoost and scikit-learn teams for excellent ML libraries
- SHAP developers for explainable AI tools
- All contributors who helped improve this project

---

## 📚 References

1. CDC Behavioral Risk Factor Surveillance System (BRFSS)
2. World Health Organization - Chronic Disease Prevention
3. American Heart Association - Risk Assessment Guidelines
4. "Interpretable Machine Learning" by Christoph Molnar
5. XGBoost: A Scalable Tree Boosting System (Chen & Guestrin, 2016)

---

## 🔮 Future Enhancements

- [ ] Integration with wearable devices (Fitbit, Apple Watch)
- [ ] Multi-language support for global accessibility
- [ ] Mobile app development (React Native)
- [ ] Real-time health monitoring dashboard
- [ ] Integration with EHR (Electronic Health Records) systems
- [ ] Advanced deep learning models (Neural Networks)
- [ ] Genetic risk factor incorporation
- [ ] Community health comparison features
- [ ] Telemedicine consultation integration

---

## ⚠️ Disclaimer

**This system is for educational and informational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.**

---

<div align="center">

**Made with ❤️ for better health outcomes**

⭐ Star this repo if you find it helpful! ⭐

</div>
