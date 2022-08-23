import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# File name
file_name = '8813_20220823'

# Read data from csv file
csv_file_name = file_name + '.csv'
csv = pd.read_csv(csv_file_name,\
                    names=['x','y','z'],\
                    encoding='CP949')

x = csv['x']
y = csv['y']
z = csv['z']

# Histogram graph
plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)

plt.hist(x, **kwargs, color='g', label='x')
plt.hist(y, **kwargs, color='b', label='y')
plt.hist(z, **kwargs, color='r', label='z')

hist_plot_tile = 'histogram plot ' + file_name
plt.gca().set(title=hist_plot_tile, ylabel='value(meter)')

plt.legend()

# 3D graph
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x, y, z, marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
scatter_plot_name = '3d scatter plot ' + file_name
ax.set_title(scatter_plot_name)

plt.show()