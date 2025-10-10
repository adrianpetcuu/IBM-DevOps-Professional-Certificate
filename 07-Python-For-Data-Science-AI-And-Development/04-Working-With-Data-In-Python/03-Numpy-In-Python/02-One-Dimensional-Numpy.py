# import numpy library
import numpy as np

# create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element
print("a[0]: ", a[0])
print("a[1]: ", a[1])
print("a[2]: ", a[2])
print("a[3]: ", a[3])
print("a[4]: ", a[4])

# Check the NumPy version
print(np.__version__)

# Check the type
print(type(a))

# Check the type of the values stored in numpy array
print(a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
print(b.dtype)

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
print(c)

# Assign the first element to 100
c[0] = 100
print(c)

# Assign the 5th element to 0
c[4] = 0
print(c)

a = np.array([10, 2, 30, 40,50])
a[1] = 20
print(a)

# Slicing the numpy array
d = c[1:4]
print(d)

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
print(c)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

print(arr[:4])

print(arr[4:])

print(arr[1:5:])

# even elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:8:2])

# assign value with list
# create the index list
select = [0, 2, 3, 4]
print(select)

# use list to select elements
d = c[select]
print(d)

# assign the specified elements to new value
c[select] = 100000
print(c)

# create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# get the size of numpy array
print(a.size)

# get the number of dimensions of numpy array
print(a.ndim)

# get the shape/size of numpy array
print(a.shape)

b = np.array([10, 20, 30, 40, 50, 60, 70])
print(b.size)
print(b.ndim)
print(b.shape)

# Numpy Statistical Functions
# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
print(mean)

# Get the standard deviation of numpy array
standard_deviation = a.std()
print(standard_deviation)

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
print(b)

# Get the biggest value in the numpy array
max_b = b.max()
print(max_b)

# Get the smallest value in the numpy array
min_b = b.min()
print(min_b)

c = np.array([-10, 201, 43, 94, 502])
max_c = c.max()
print(max_c)
min_c = c.min()
print(min_c)
Sum = (max_c + min_c)
print(Sum)

# Array addition
u = np.array([1, 0])
print(u)
v = np.array([0, 1])
print(v)
# Numpy Array Addition
z = np.add(u, v)
print(z)

# Plotting function
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

def Plotvec1(u, v, z):
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1) # Add an arrow to the U axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u') # Adds the text u to the Axes

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1) # Add an arrow to the V axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(v + 0.1), 'v') # Adds the text v to the Axes

    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z') # Adds the text z to the axes
    plt.ylim(-2, 2) # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2) # set the xlim to left(-2), right(2)
    plt.show()

# Plot numpy arrays
Plotvec1(u, v, z)


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.add(arr1, arr2)
print(arr3)

# Array subtraction
a = np.array([10, 20, 30])
print(a)
b = np.array([5, 10, 15])
print(b)
c = np.subtract(a, b)
print(c)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.subtract(arr1, arr2)
print(arr3)

# Array Multiplication
x = np.array([1, 2])
print(x)

y = np.array([2, 1])
print(y)

z = np.multiply(x, y)
print(z)

# Numpy Array Multiplication
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])
arr3 = np.multiply(arr1, arr2)
print(arr3)

# Array Division
a = np.array([10, 20, 30])
print(a)
b = np.array([2, 10, 5])
print(b)
c = np.divide(a, b)
print(c)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
arr3 = np.divide(arr1, arr2)
print(arr3)

# Dot Product
X = np.array([1, 2])
Y = np.array([3, 2])
# Calculate the dot product
print(np.dot(X, Y))
# Elements of X
print(X[0])
print(X[1])
# Elements of Y
print(Y[0])
print(Y[1])

arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
arr3 = np.dot(arr1, arr2)
print(arr3)

# Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1])
print(u)
# Add the constant to array
print(u + 1)

arr = np.array([1, 2, 3, -1])
print(arr + 5)


# Mathematical Functions
# The value of pi
print(np.pi)
# Create the numpy array in radians
x = np.array([0, np.pi/2, np.pi])
# Calculate the sin of each elements
y = np.sin(x)
print(y)

# Linspace
# Makeup a numpy array within [-2, 2] and 5 elements
print(np.linspace(-2, 2, num=5))

# Make a numpy array within [-2, 2] and 9 elements
print(np.linspace(-2, 2, num=9))

# Make a numpy array within [0, 2pi] and 100 elements
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)
plt.show()

# Make a numpy array within [5, 4] and 6 elements
print(np.linspace(5, 4, num=6))

# Iterating 1-D Arrays
arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
    print(x)

# Implement the vector subtraction in numpy: u-v
u = np.array([1, 0])
v = np.array([0, 1])
z = np.subtract(u, v)
print(z)

# Multiply the numpy array z with -2
z = np.array([2, 4])
z = np.multiply(-2, z)
print(z)

# Multiply them together
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
c = np.multiply(a, b)
print(c)

# Import the libraries

import time
import sys
import numpy as np

import matplotlib.pyplot as plt


def Plotvec2(a, b):
    ax = plt.axes()  # to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)  # Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)  # Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)  # set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)  # set the xlim to left(-2), right(2)
    plt.show()

# Plot the arrays as vectors using the function Plotvec2 and find their dot product
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is ", np.dot(a, b))

a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

# Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2.
# Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2.
arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
print(arr3)

arr4 = np.subtract(arr1, arr2)
print(arr4)

arr5 = np.multiply(arr1, arr2)
print(arr5)

arr6 = np.divide(arr1, arr2)
print(arr6)

arr7 = np.dot(arr1, arr2)
print(arr7)

# Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2.
# Then find the even and odd numbers from arr1 and arr2.
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1: ", even_arr1)

# Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1 = arr1[0:5:2]
print("odd for array1: ", odd_arr1)

# Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2: ", even_arr2)

# Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2 = arr2[1:5:2]
print("odd for array2: ", odd_arr2)
