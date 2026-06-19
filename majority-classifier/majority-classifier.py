import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    n = len(X_test)
    if n==0: return []

    classes, first_indices, counts = np.unique(y_train, return_index=True, return_counts=True)

    max_count = np.max(counts)
    indices = np.where(counts == max_count)[0]
    if len(indices)>1:
        original = first_indices[indices]
        majority_class = classes[indices[np.argmin(original)]]
    else:
        majority_class = classes[indices[0]]
    predictions = np.full(shape=n, fill_value=majority_class, dtype=int)
    return predictions