import numpy as np
from typing import List

"""
    Brownian Motion K dimension.
"""
def BrowniankD(t0: float = 0, t1: float = 1., N: int = 10000, ndim: int = 4, nums: int = 3, mean: List[float] = (0)):
    
    if not isinstance(mean, (tuple, list)) or len(mean) != ndim:
        mean = [0] * ndim

    timeSpace = np.linspace(t0, t1, N, endpoint=True, dtype=np.float64)
    dt = timeSpace[1] - timeSpace[0]

    mean = np.array(mean, dtype=np.float64)
    mean = np.expand_dims(mean, 0)
    mean = mean.repeat(nums, axis=0)
    mean = np.expand_dims(mean, 0)

    std = np.sqrt(np.array([dt] * ndim, dtype=np.float64))
    std = np.expand_dims(std, 0)
    std = std.repeat(nums, 0)

    print(mean.shape)
    print(std.shape)

    dB = std * np.random.normal(size=(N - 1, nums, ndim))
    
    B = np.cumsum(dB, axis=0, dtype=np.float64) + mean
    B = np.concatenate((mean, B))
    
    return B
    
if __name__ == "__main__":
    Data = BrowniankD(t0=0, t1=1., N=10000, ndim=4, nums=3, mean=(3, 4, 1, 3))
    print(Data)