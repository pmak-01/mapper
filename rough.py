import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt", delimiter=',')
x = data[:, 0]
y = data[:, 1]
plt.plot(x, y, 'ro')
plt.xlim(0, 1150)
plt.ylim(0, 2000)
plt.show()
