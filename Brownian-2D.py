import numpy as np
from matplotlib import pyplot as plt
from typing import List
from matplotlib import style

style.use("ggplot")

"""
    Brownian motion in 2D.
    Keep the number of intervals below 100
     to get a good plot.
"""

def Brownian2D(t0: float = 0, t1: float = 1., N: int = 10000, nums: int = 1, mean: List[float] = (0, 0)):
    timeSpace = np.linspace(t0, t1, num=N, endpoint=True, dtype=np.float64)
    dt = timeSpace[1] - timeSpace[0]

    std = np.sqrt([dt] * 2, dtype=np.float64)
    std = np.expand_dims(std, 0)
    std = std.repeat(nums, 0)

    mean = np.array(mean, dtype=np.float64)
    mean = np.expand_dims(mean, 0)
    mean = mean.repeat(nums, 0)
    mean = np.expand_dims(mean, 0)

    dB = np.random.normal(size=(N - 1, nums, 2))
    B = np.cumsum(dB, axis=0)
    B = mean + B

    B = np.concatenate((mean, B))
    print(B.shape)

    ax = plt.axes(projection='3d')

    for i in range(nums):
        ax.plot3D(B[:, i, 0].flatten(), B[:, i, 1].flatten(), timeSpace)
    
    plt.show()

    return B


if __name__ == "__main__":
    Brownian2D(0, 1., 100, 3, (3, 2))