# Import the library

import matplotlib.pyplot as plt
%matplotlib inline

# Plot
plt.plot([1,2,3,4,10])
#> [<matplotlib.lines.Line2D at 0x10edbab70>]

# 1D Data
import numpy as np
x = np.linspace(0, 10, 100)
y = np.cos(x) 
z = np.sin(x)

#2D Data
data = 2 * np.random.random((10, 10))
data2 = 3 * np.random.random((10, 10))
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
from matplotlib.cbook import get_sample_data
img = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))


