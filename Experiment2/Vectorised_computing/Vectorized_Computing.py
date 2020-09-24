# Import the required library
import numpy as np

# Create a 2D array.
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0][2])

# Create a 3D array.
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
old_values = arr3d[0].copy()
print(old_values)
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)

array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], dtype='<U4')
names == 'Bob'

# Mathenatical application
arr = np.arange(10)
r=np.sqrt(arr)
e=np.exp(arr)
print("Sqrt= ",r,"\n Exp= ",e)

'''As a simple example, suppose we wished to evaluate the function sqrt(x^2 + y^2) across a regular grid of values.
The np.meshgrid function takes two 1D arrays and produces two 2D matrices corresponding to all pairs of (x, y) in the two arrays'''

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)

'''evaluating the function is a matter of writing the same expression you would write with two points:'''

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
