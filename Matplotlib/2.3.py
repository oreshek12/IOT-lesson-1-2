import numpy as np
import matplotlib.pyplot as plt

num_points = 150


r_min = 0
r_max = 2
theta_min = 0
theta_max = 360
r = np.random.uniform(r_min, r_max, num_points)
theta = np.random.uniform(theta_min, theta_max, num_points)
theta_rad = np.deg2rad(theta)
x = r * np.cos(theta_rad)
y = r * np.sin(theta_rad)

plt.figure(figsize=(6, 6))
plt.axes(projection='polar')
plt.scatter(theta, r)
plt.scatter(theta, r,
 s=400*r**2,
 c=theta,
 cmap='hsv',
 alpha=0.8
 )
