from joblib import dump, load
import pandas as pd
import numpy as np
from .data_processor import log_txf, remap_emp_length

def get_prediction(**kwargs):
    clf = load('models/mdl.joblib')
    features = load('models/raw_features.joblib')
    pred_df = pd.DataFrame(kwargs, index=[0])
    pred_df = log_txf(pred_df, ['annual_inc'])
    pred_df['emp_len'] = pred_df['emp_length'].map(remap_emp_length)
    pred = clf.predict(pred_df[features])
    return pred[0]
