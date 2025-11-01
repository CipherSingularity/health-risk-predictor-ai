import joblib
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'artifacts' / 'preprocessor.pkl'
print('Preprocessor path:', p)
pre = joblib.load(p)
try:
    cols = list(pre.feature_names_in_)
    print('feature_names_in_:', cols)
except AttributeError:
    # older sklearn
    print('feature_names_in_ not available; try pre.get_feature_names_out() or inspect transformers')

# Also show transformers' columns if present
try:
    for name, trans, cols in pre.transformers:
        print('transformer:', name, 'cols:', cols)
except Exception as e:
    print('Could not inspect transformers:', e)
