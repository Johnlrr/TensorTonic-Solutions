import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    mean = np.mean(y_true)
    if np.sum((y_true-mean)**2)==0:
        if np.array_equal(y_true, y_pred): return 1
        else: return 0
    return (1 - np.sum((y_true-y_pred)**2)/np.sum((y_true-mean)**2))