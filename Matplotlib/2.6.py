import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
 return (x - 1)**2 - (y + 2)**2
x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)

X, Y = np.meshgrid(x, y)
Z = func(X, Y) #Матрица z

fig, ax = plt.subplots(1, 1, figsize=(6, 5))
obj = ax.imshow(Z, cmap=plt.cm.seismic, vmin=-400, vmax=400)

fig.colorbar(obj, vmin=-400, vmax=400)


