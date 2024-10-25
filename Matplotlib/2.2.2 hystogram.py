import numpy as np
import matplotlib.pyplot as plt


x_min = -5 * np.pi
x_max = 5 * np.pi
num_points = 10000000
x = np.linspace(x_min, x_max, num_points)


y1 = np.random.normal(-10, 7, num_points)
y2 = np.random.normal(10, 5, num_points)
y3 = np.random.normal(25, 10, int(1.5 * num_points))


y = np.concatenate([y1, y2, y3])


plt.hist(y, bins=100)  
