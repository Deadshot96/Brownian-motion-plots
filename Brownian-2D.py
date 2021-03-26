import numpy as np
from matplotlib import pyplot as plt
from typing import Tuple
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

style.use("ggplot")

"""
    Brownian motion in 2D.
    Keep the number of intervals below 100
     to get a good plot.
"""

def Brownian2D(t0: float = 0, t1: float = 1., N: int = 10000, nums: int = 1):
    timeSpace = np.linspace(t0, t1, num=N, endpoint=True, dtype=np.float64)
    dt = timeSpace[1] - timeSpace[0]

    mean = np.array([(0, 0)], dtype=np.float64)
    mean = mean.repeat(repeats=nums, axis=0)
    stdDev = np.sqrt(np.array([dt, dt], dtype=np.float64))
    stdDev = np.expand_dims(stdDev, 0)

    mean = np.expand_dims(mean, axis=0)
    # print(mean)

    dB = stdDev * np.random.normal(size=(N - 1, nums, 2), loc=mean)
    B = np.cumsum(dB, axis=0)
    
    B = np.concatenate((mean, dB))

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    for i in range(nums):
        ax.plot3D(B[:, i, 0].flatten(), B[:, i, 1].flatten(), timeSpace)
    
    plt.show()


if __name__ == "__main__":
    Brownian2D(0, 1., 100, 1)