import numpy as np
from matplotlib import pyplot as plt

def quadratic_variation(B):
    return np.cumsum(np.power(np.diff(B, axis=0, prepend=0.), 2), axis=0)

def Brownian1D(t0: int = 0, t1: int = 1, N: int = 10000, nums: int = 1):
    timeSpace = np.linspace(t0, t1, num=N, endpoint=True, dtype=np.float64)
    
    dt = timeSpace[1] - timeSpace[0]
    mean = np.zeros(shape = (0, nums), dtype=np.float64)
    stdDev = np.sqrt(dt)

    dB = stdDev * np.random.normal(size=(N - 1, nums))

    
    B = np.concatenate((np.zeros(shape=(1, nums)), np.cumsum(dB, axis=0, dtype=np.float64)), 0)
    print(B[100])
    
    plt.plot(timeSpace, B)
    # plt.plot(timeSpace, quadratic_variation(B))

    plt.show()

    # print(timeSpace)


if __name__ == "__main__":
    Brownian1D(0, 1, 10000, 7)