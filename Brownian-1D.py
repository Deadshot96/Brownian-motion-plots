import numpy as np
from matplotlib import pyplot as plt

def quadratic_variation(B):
    return np.cumsum(np.power(np.diff(B, axis=0, prepend=0.), 2), axis=0)

def Brownian1D(t0: int = 0, t1: int = 1, N: int = 10000, nums: int = 1, mean:float = 0.0):
    timeSpace = np.linspace(t0, t1, num=N, endpoint=True, dtype=np.float64)
    
    dt = timeSpace[1] - timeSpace[0]
    
    mean = np.array([mean], dtype=np.float64)
    mean = mean.repeat(nums)
    # mean = np.expand_dims(mean, 0)
    print(mean)

    stdDev = np.sqrt([dt] * nums)
    print(stdDev)

    # print(mean.shape)
    dB = stdDev * np.random.normal(size=(N - 1, nums)) + mean
    print(dB[0])
    print(dB[1])

    # print(dB.shape)
    B = np.cumsum(dB, axis=0, dtype=np.float64)
    print(B[0])
    print(B[1])
    
    B = np.concatenate((mean, B), 0)
    # print(B.shape)
    
    plt.plot(timeSpace, B)
    # plt.plot(timeSpace, quadratic_variation(B))

    plt.show()

    # print(timeSpace)

    return B


if __name__ == "__main__":
    Brownian1D(0, 1, 10000, 7, 1)