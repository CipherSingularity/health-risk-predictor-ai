import joblib
from pathlib import Path
p=Path(__file__).resolve().parents[1] / 'artifacts' / 'preprocessor.pkl'
pre=joblib.load(p)
enc=pre.named_transformers_['cat']
print('encoder drop:', enc.drop)
print('encoder handle_unknown:', getattr(enc,'handle_unknown', None))
print('get_feature_names_out:', enc.get_feature_names_out(['Gender','BMI_Category','Age_Group']))
