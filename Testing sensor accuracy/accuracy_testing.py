import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [64.83, 64.83, 65.86, 65.86, 64.83, 65.86, 65.86, 65.68, 64.83, 65.86],
    [107.53, 108.56, 107.53, 108.56, 107.53, 108.56, 107.53, 108.56, 107.53, 108.56],
    [156.07, 156.24, 156.07, 157.27, 156.07, 156.24, 156.07, 156.24, 157.09, 156.07],
    [205.80, 205.80, 205.80, 204.60, 204.60, 205.80, 205.80, 205.63, 203.06, 203.23],
    [248.16, 248.16, 249.19, 248.16, 248.16, 249.19, 247.99, 245.59, 246.62, 248.16],
    [308.01, 307.84, 308.70, 308.70, 308.70, 309.73, 303.55, 308.70, 309.73, 308.70],
    [359.64, 354.66, 350.37, 355.69, 355.52, 352.09, 352.26, 354.66, 354.83, 355.69],
    [398.39, 397.37, 398.39, 398.39, 395.82, 395.82, 397.19, 397.37, 402.51, 402.51],
    [451.90, 452.93, 451.90, 452.93, 446.76, 452.93, 451.90, 452.93, 451.73, 452.93]
])
'''Distances (in mm) measured when sensor was facing a wall straight ahead. 
In successive rows, sensor was moved 50mm away from wall'''

data -= 1 # systematic error of 1 mm

pos = np.arange(50, 460, 50).reshape(9, 1)
'''Actual distance from wall straight ahead'''

error = data - pos
error_percent = error / data * 100.
print(error_percent)

plt.plot(pos, error_percent, 'bo')
plt.xlabel("Distance measured (in mm)")
plt.ylabel("Error %")
plt.title("Measurement error percentage vs. distance measured")
plt.show()