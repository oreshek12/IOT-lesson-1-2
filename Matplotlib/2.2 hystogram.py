import numpy as np
import matplotlib.pyplot as plt

# Генерация данных по распределению Коши
y = np.random.standard_cauchy(10000000)

plt.hist(y,
 range=(0, 5),
 bins=50,
 density=True
 )