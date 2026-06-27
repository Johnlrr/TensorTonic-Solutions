import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.array(matrix)
    if matrix.ndim != 2: 
        return None
    if axis not in [None,0,1]:
        return None

    
    if norm_type == 'l2':
        norm = np.sqrt(np.sum(np.square(matrix), axis=axis, keepdims=True))
    elif norm_type == 'l1':
        norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
    elif norm_type == 'max':
        norm = np.max(np.abs(matrix), axis=axis, keepdims=True)
    else:
        return None
    
    norm[norm==0.0] = 1.0
    return matrix/norm