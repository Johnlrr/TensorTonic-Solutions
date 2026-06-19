import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    TP = np.sum((y_true==y_pred))
    FP_FN = np.sum(y_true != y_pred) * 2
    return 2*TP/(2*TP + FP_FN)