import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    mode = float(np.min(modes))
    return [mean, median, mode]