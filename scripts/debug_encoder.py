import joblib
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'artifacts' / 'preprocessor.pkl'
pre = joblib.load(p)
enc = pre.named_transformers_['cat']
print('Encoder:', type(enc))
for i, cats in enumerate(enc.categories_):
    print(i, cats, 'dtype:', cats.dtype, 'sample types:', [type(x) for x in cats[:5]])

print('\nTransformers_ info:')
for t in pre.transformers_:
    print(t[0], t[2])
