import numpy as np
import matplotlib.pyplot as plt

measure_min, measure_max = 20, 4000

def clean_data(data: np.ndarray, d_max: float) -> list[np.ndarray]:
    dist_data = data[:, :-2]
    x_correction = data[:, -2].reshape(data.shape[0], 1)
    y_correction = data[:, -1].reshape(data.shape[0], 1)
    dist_data[dist_data < measure_min] = np.nan
    dist_data[dist_data > min(d_max, measure_max)] = np.nan
    return [dist_data, x_correction, y_correction]

def get_coords(angle, dist_data, x_correction, y_correction, x_lim, y_lim, tolerance: int):
    x = dist_data*np.cos(angle)
    y = dist_data*np.sin(angle)
    x += x_correction
    y += y_correction

    x[x < x_lim[0]-tolerance] = np.nan
    x[x > x_lim[1]+tolerance] = np.nan
    y[y < y_lim[0]-tolerance] = np.nan
    y[y > y_lim[1]+tolerance] = np.nan

    return x, y

# x_correction = np.arange(50, 650+1, 50).reshape(dist_data.shape[0], 1)
# y_correction = np.zeros(dist_data.shape[0]).reshape(dist_data.shape[0], 1)
# x_correction = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]).reshape(dist_data.shape[0], 1)
# y_correction = np.arange(300, -1, -50).reshape(dist_data.shape[0], 1)