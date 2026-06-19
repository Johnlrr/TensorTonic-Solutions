import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    nl = len(y_left)
    nr = len(y_right)
    n = nl+nr
    
    _, counts_l = np.unique(y_left, return_counts=True)
    if nl==0:
        gini_l = 0.0
    else:
        probs_l = counts_l/nl
        gini_l = 1.0 - np.sum(probs_l**2)

    _, counts_r = np.unique(y_right, return_counts=True)
    if nr==0:
        gini_r = 0.0
    else:
        probs_r = counts_r/nr
        gini_r = 1.0 - np.sum(probs_r**2)

    if n==0:
        return 0.0

    gini = (nl/n)*gini_l + (nr/n)*gini_r
    return gini    
    