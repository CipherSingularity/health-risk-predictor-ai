# src/prediction.py
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Iterable


def _locate_file(filename: str, search_dirs: Iterable[Path]):
    """Search for filename in provided directories and return first matching Path.

    Raises FileNotFoundError with a helpful message if not found.
    """
    for d in search_dirs:
        p = d / filename
        if p.exists():
            return p
    searched = ', '.join(str(d) for d in search_dirs)
    raise FileNotFoundError(f"Could not find '{filename}' in: {searched}")


def predict_risk(input_dict):
    # Resolve repository root and candidate artifact/model folders
    repo_root = Path(__file__).resolve().parents[1]
    candidates = [repo_root / 'models', repo_root / 'artifacts', repo_root]

    # Attempt to load separate scaler + per-disease models. If those aren't available,
    # fall back to a multi-output chronic model + preprocessor saved in artifacts.
    models = {}
    scaler = None
    try:
        scaler_path = _locate_file('scaler.pkl', candidates)
        scaler = joblib.load(scaler_path)

        model_files = {
            'diabetes': 'diabetes_model.pkl',
            'heart_disease': 'heart_disease_model.pkl',
            'stroke': 'stroke_model.pkl'
        }

        for name, fname in model_files.items():
            path = _locate_file(fname, candidates)
            models[name] = joblib.load(path)
    except FileNotFoundError:
        # Try fallback: a single multi-output model saved by the notebook (e.g. chronic_disease_model.pkl)
        try:
            chronic_path = _locate_file('chronic_disease_model.pkl', candidates)
            chronic_model = joblib.load(chronic_path)
            # Try to load a preprocessor if available to transform raw input
            try:
                preproc_path = _locate_file('preprocessor.pkl', candidates)
                preprocessor = joblib.load(preproc_path)
            except FileNotFoundError:
                preprocessor = None

            # Build df below as usual, then use preprocessor to transform
            # and extract probabilities from the multi-output model.
            # We'll set models to a special marker and handle later.
            models = {'__multi__': (chronic_model, preprocessor)}

        except FileNotFoundError as e:
            # Re-raise earlier, with a clear message about what we searched for
            raise FileNotFoundError(
                "No scaler/models found and no chronic multi-output model available. "
                "Searched locations: {}".format(', '.join(str(p) for p in candidates))) from e

    # Build DataFrame with expected columns (fallback values)
    df = pd.DataFrame([input_dict])
    df = df.reindex(columns=[
        'Age', 'Gender', 'Glucose', 'HbA1c', 'Systolic', 'Diastolic', 'BMI', 'Cholesterol',
        'Triglycerides', 'Smoking', 'Alcohol', 'Physical_Activity', 'Diet_Score',
        'Family_History', 'Sleep_Hours', 'Stress_Level', 'TC_HDL_Ratio'
    ], fill_value=0)

    # Ensure TC_HDL_Ratio exists sensibly
    if (pd.isna(df.loc[0, 'TC_HDL_Ratio']) or df.loc[0, 'TC_HDL_Ratio'] == 0) and 'Cholesterol' in df.columns:
        # Use a safe divisor if HDL not provided; this is a fallback only
        df['TC_HDL_Ratio'] = df['Cholesterol'] / 50

    # Coerce numeric columns to numeric to avoid dtype issues
    numeric_cols = ['Age', 'Glucose', 'HbA1c', 'Systolic', 'Diastolic', 'BMI', 'Cholesterol',
                    'Triglycerides', 'Smoking', 'Alcohol', 'Physical_Activity', 'Diet_Score',
                    'Family_History', 'Sleep_Hours', 'Stress_Level', 'TC_HDL_Ratio']
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)

    # If we have the multi-output chronic model, use its preprocessor (if present) to transform
    if '__multi__' in models:
        chronic_model, preprocessor = models['__multi__']
        if preprocessor is not None:
            # Align and populate the raw DataFrame to match preprocessor.feature_names_in_
            expected = list(preprocessor.feature_names_in_)

            def _candidates(name):
                # generate possible input keys that map to this expected column
                yield name
                yield name.replace(' ', '_')
                yield name.replace(' ', '').lower()
                yield name.lower().replace(' ', '_')

            df_aligned = pd.DataFrame(index=df.index)
            for col in expected:
                found = False
                for cand in _candidates(col):
                    if cand in df.columns:
                        df_aligned[col] = df[cand]
                        found = True
                        break
                if not found:
                    # handle some common derived/renamed columns
                    if col == 'Systolic_BP' and 'Systolic' in df.columns:
                        df_aligned[col] = pd.to_numeric(df['Systolic'], errors='coerce')
                    elif col == 'Diastolic_BP' and 'Diastolic' in df.columns:
                        df_aligned[col] = pd.to_numeric(df['Diastolic'], errors='coerce')
                    elif col == 'BMI_Category' and 'BMI' in df.columns:
                        df_aligned[col] = pd.cut(pd.to_numeric(df['BMI'], errors='coerce'), bins=[0,18.5,25,30,100], labels=['Underweight','Normal','Overweight','Obese'])
                    elif col == 'Age_Group' and 'Age' in df.columns:
                        df_aligned[col] = pd.cut(pd.to_numeric(df['Age'], errors='coerce'), bins=[0,40,60,100], labels=['Young','Middle','Senior'])
                    else:
                        # default to NaN
                        df_aligned[col] = pd.NA

            # Identify categorical columns and their default fill values from the fitted OneHotEncoder
            cat_cols = []
            cat_fill = {}
            try:
                # transformers_ entries: ('num', transformer, cols), ('cat', transformer, cols)
                for name, transformer, cols in preprocessor.transformers_:
                    if name == 'cat':
                        cat_cols = list(cols)
                        try:
                            enc = preprocessor.named_transformers_['cat']
                            # enc.categories_ is a list parallel to cat_cols
                            for i, col in enumerate(cat_cols):
                                cats = enc.categories_[i] if hasattr(enc, 'categories_') else []
                                cat_fill[col] = cats[0] if len(cats) > 0 else ''
                        except Exception:
                            for col in cat_cols:
                                cat_fill[col] = ''
                        break
            except Exception:
                cat_cols = []

            # Coerce numeric columns to numeric (safe) and fill categorical cols with a default category
            for c in df_aligned.columns:
                if c in cat_cols:
                    # ensure object dtype before filling with string category
                    df_aligned[c] = df_aligned[c].astype(object).fillna(cat_fill.get(c, ''))
                else:
                    df_aligned[c] = pd.to_numeric(df_aligned[c], errors='coerce').fillna(0)

            # DEBUG: print alignment and category info to help trace empty prediction cases
            try:
                print('\n--- prediction debug: df_aligned ---')
                print('columns:', list(df_aligned.columns))
                print('row0:', df_aligned.iloc[0].to_dict())
                print('cat_cols:', cat_cols)
                if 'enc' in locals():
                    print('encoder categories:', [[str(x) for x in cats] for cats in enc.categories_])
            except Exception:
                pass

            # Manually assemble transformed matrix to avoid OneHotEncoder transform bug
            # 1) numeric transformer
            try:
                num_cols = list(preprocessor.transformers_[0][2])
                num_transformer = preprocessor.named_transformers_['num']
                num_array = num_transformer.transform(df_aligned[num_cols])
            except Exception:
                # fallback: numeric values as-is
                num_cols = [c for c in df_aligned.columns if c not in cat_cols]
                num_array = df_aligned[num_cols].to_numpy()

            # 2) categorical: build one-hot columns respecting drop='first'
            cat_matrix = np.zeros((len(df_aligned), 0))
            try:
                enc = preprocessor.named_transformers_['cat']
                cat_cols_local = list(preprocessor.transformers_[1][2])
                cat_arrays = []
                for i, col in enumerate(cat_cols_local):
                    cats = enc.categories_[i]
                    # drop first category per encoder configuration
                    for cat in cats[1:]:
                        # compare case-insensitively to be robust to capitalization differences
                        left = df_aligned[col].astype(str).str.lower()
                        right = str(cat).lower()
                        arr = (left == right).astype(int).to_numpy().reshape(-1, 1)
                        cat_arrays.append(arr)
                # DEBUG: report categorical matrix stats
                try:
                    if cat_arrays:
                        print('cat_arrays count:', len(cat_arrays), 'first col sample:', cat_arrays[0].ravel()[:5])
                except Exception:
                    pass
                if cat_arrays:
                    cat_matrix = np.hstack(cat_arrays)
                else:
                    cat_matrix = np.zeros((len(df_aligned), 0))
            except Exception:
                cat_matrix = np.zeros((len(df_aligned), 0))

            # 3) concatenate numeric + categorical arrays to form X_proc
            if num_array.size == 0 and cat_matrix.size == 0:
                X_proc = df_aligned.to_numpy()
            else:
                X_proc = np.hstack([num_array, cat_matrix])
        elif scaler is not None:
            # if scaler was somehow set, use it
            X_proc = scaler.transform(df)
        else:
            # try to coerce numeric and pass raw
            X_proc = df.values

        proba_list = chronic_model.predict_proba(X_proc)
        # proba_list is a list/tuple of (n_samples, n_classes) arrays, one per target
        target_names = ['diabetes', 'heart_disease', 'stroke']
        results = {}
        for i, arr in enumerate(proba_list):
            try:
                prob_pos = float(arr[0][1])
            except Exception:
                prob_pos = float(arr[0]) if arr.shape[1] == 1 else float('nan')
            results[target_names[i]] = round(prob_pos * 100, 1)
        return results

    # Otherwise use separate scaler + models
    X = scaler.transform(df)
    results = {}
    for name, model in models.items():
        proba = model.predict_proba(X)[0][1]
        results[name] = round(proba * 100, 1)

    return results