# src/prediction.py
import joblib
import pandas as pd
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
            X_proc = preprocessor.transform(df)
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