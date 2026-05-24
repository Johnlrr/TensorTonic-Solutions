import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        return None

    N = X.shape[0]
    if N <= 1:
        return None
    mean = np.mean(X, axis=0)
    x = X - mean
    cov = (1/(N - 1))*(x.T @ x)
    return cov