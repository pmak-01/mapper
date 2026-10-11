import numpy as np
import matplotlib.pyplot as plt
from serial_talker import read_serial
from analysis import clean_data, get_coords

angle_lim, del_angle = (30, 150), 10
x_lim = (0, 750)
y_lim = (0, 450)
tolerance = 50

d_max = np.sqrt((x_lim[1]-x_lim[0])**2 + (y_lim[1]-y_lim[0]**2))

choose_function = input("Enter 1 to visualize existing data or 2 to record and append new data ").strip()
if choose_function == '2':
    read_serial('COM3', 9600) # replace `COM3` with the port name on your laptop

data = data = np.loadtxt('data.txt', delimiter=',', converters=float)
x = data[:, 0]
y = data[:, 1]

angle = np.arange(angle_lim[0], angle_lim[1]+1, del_angle) * np.pi / 180.0

dist_data, x_correction, y_correction = clean_data(data, d_max)
x, y = get_coords(angle, dist_data, x_correction, y_correction, x_lim, y_lim, tolerance)

plt.plot(x, y, 'bo')
plt.show()