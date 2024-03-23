import numpy as np
from pprint import pprint

def calculate(arr):
    if len(arr) != 9:
        raise ValueError("List must have at least 9 elements.")
    
    nums = np.array(arr).reshape([3, 3])
    
    calculations = {
        'mean': [nums.mean(0).tolist(), nums.mean(1).tolist(), nums.mean()],
        'variance': [nums.var(0).tolist(), nums.var(1).tolist(), nums.var()],
        'standard deviation': [nums.std(0).tolist(), nums.std(1).tolist(), nums.std()],
        'max': [nums.max(0).tolist(), nums.max(1).tolist(), nums.max()],
        'min': [nums.min(0).tolist(), nums.min(1).tolist(), nums.min()],
        'sum': [nums.sum(0).tolist(), nums.sum(1).tolist(), nums.sum()]
        }

    return calculations

pprint(calculate([i for i in range(0, 9)]))
