import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
 return -np.sqrt(x**2+y**2)
x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)

X, Y = np.meshgrid(x, y)
I = func(X, Y) 

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
mapp = ax.pcolormesh(X, Y, I, cmap='inferno', shading='auto',
edgecolor='face')
fig.colorbar(mapp)