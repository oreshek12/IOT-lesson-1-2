import numpy as np
import matplotlib.pyplot as plt
import random


x_min = -5
x_max = 5
num_points = 40


x = np.linspace(x_min, x_max, num_points)


y = np.sin(x) + np.tan(2 * (x - 2))


yerr = [random.uniform(1, 2) for _ in range(num_points)]  #функция  random.sample не выполняется выдавая ошибку Sample larger than population or is negative поэтому заменена на эту 


plt.figure(figsize=(10, 5))
plt.errorbar(x, y,
 yerr=yerr,
 ecolor='forestgreen', 
 capsize=10,
 elinewidth=1.5 
 )
