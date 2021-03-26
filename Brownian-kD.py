import numpy as np

"""
    Brownian Motion K dimension.
"""
def BrowniankD(t0: float = 0, t1: float = 1., N: int = 10000, k: int = 4, nums: int = 3):
    
    timeSpace = np.linspace(t0, t1, N, endpoint=True, dtype=np.float64)
    dt = timeSpace[1] - timeSpace[0]

    mean = [0] * k
    mean = np.array(mean, dtype=np.float64)
    mean = np.expand_dims(mean, 0)
    mean = mean.repeat(nums, axis=0)
    mean = np.expand_dims(mean, 0)

    stdDev = [dt] * k
    stdDev = np.sqrt(np.array(stdDev, dtype=np.float64))
    stdDev = np.expand_dims(stdDev, 0)

    # print(mean.shape)
    # print(stdDev)

    dB = stdDev * np.random.normal(size=(N - 1, nums, k))
    
    B = np.cumsum(dB, axis=0, dtype=np.float64)
    B = np.concatenate((mean, B))
    
    return B
    
if __name__ == "__main__":
    BrowniankD(0, 1., 10000, 4, 3)
