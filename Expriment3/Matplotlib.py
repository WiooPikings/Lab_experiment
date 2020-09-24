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

# Creating plot
import matplotlib.pyplot as plt
fig = plt.figure()
fig2 = plt.figure(figsize=plt.figaspect(2.0))
fig.add_axes()
ax1 = fig.add_subplot(221) # row-col-num
ax3 = fig.add_subplot(212) 
fig3, axes = plt.subplots(nrows=2,ncols=2)
fig4, axes2 = plt.subplots(ncols=3)

#1D Data ploting
lines = ax.plot(x,y)      #       Draw points with lines or markers connecting them
ax.scatter(x,y)            #      Draw unconnected points, scaled or colored
axes[0,0].bar([1,2,3],[3,4,5]) #  Plot vertical rectangles (constant width)       
axes[1,0].barh([0.5,1,2.5],[0,1,2]) #  Plot horiontal rectangles (constant height)
axes[1,1].axhline(0.45)        #  Draw a horizontal line across axes   
axes[0,1].axvline(0.65)       #   Draw a vertical line across axes
ax.fill(x,y,color='blue')      #   Draw filled polygons 
ax.fill_between(x,y,color='yellow') # Fill between y-values and 0

#2D image or data
fig, ax = plt.subplots()
im = ax.imshow(img,Colormapped or RGB arrayscmap='gist_earth',interpolation='nearest',vmin=-2,vmax=2)

# Vector field
axes[0,1].arrow(0,0,0.5,0.5) #   Add an arrow to the axes
axes[1,1].quiver(y,z)          # Plot a 2D field of arrows
axes[0,1].streamplot(X,Y,U,V) # Plot 2D vector fields

# Data Distribution
ax1.hist(y)       #    Plot a histogram
ax3.boxplot(y)     #   Make a box and whisker plot
ax3.violinplot(z)    # Make a violin plot

# Save figures
plt.savefig('foo.png') #   Save transparent figures
plt.savefig('foo.png', transparent=True)

# Show plot
plt.show()

# Clear and Close
plt.cla()      #         Clear an axis
plt.clf()        #       Clear the entire figure
plt.close()        #     Close a window
