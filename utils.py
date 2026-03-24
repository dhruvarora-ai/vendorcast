import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

def evaluate(y_true, preds):
    mae = mean_absolute_error(y_true, preds)
    r2 = r2_score(y_true, preds)
    acc = max(0, 100 - (mae / (np.mean(y_true)+1e-5)) * 100)
    return mae, r2, acc