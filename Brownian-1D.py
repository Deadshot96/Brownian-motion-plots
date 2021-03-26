import numpy as np
from matplotlib import pyplot as plt


def Brownian1D(t0: int = 0, t1: int = 1, N: int = 10000, nums: int = 1, mean:float = 0.0):
    timeSpace = np.linspace(t0, t1, num=N, endpoint=True, dtype=np.float64)
    
    dt = timeSpace[1] - timeSpace[0]
    
    mean = np.array(mean, dtype=np.float64)
    mean = mean.repeat(nums)
    mean = np.expand_dims(mean, 0)

    stdDev = np.sqrt([dt] * nums)

    dB = stdDev * np.random.normal(size=(N - 1, nums))

    B = np.cumsum(dB, axis=0, dtype=np.float64) + mean
    
    B = np.concatenate((mean, B), 0)
    
    plt.plot(timeSpace, B)
    plt.xlabel("Time - t")
    plt.ylabel("Space - x")
    plt.title("Brownian Motion 1-D")
    plt.show()

    return B


if __name__ == "__main__":
    Brownian1D(0, 1, 10000, 4, 12)