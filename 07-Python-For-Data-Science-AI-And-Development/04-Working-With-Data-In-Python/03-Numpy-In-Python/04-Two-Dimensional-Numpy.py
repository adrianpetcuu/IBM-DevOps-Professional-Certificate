# Import the libraries
import numpy as np

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# Convert list to Numpt Array
# Every element is the same type
A = np.array(a)
print(A)

# Show the numpy array dimensions
print(A.ndim)

# Show the numpy array shape
print(A.shape)

# Show the numpy array size
print(A.size)

# Access the element on the second raw and third column
print(A[1, 2])

# Access the element on the second tow and third column
print(A[1][2])

# Access the element on the first row and first column
print(A[0][0])

# Access the element on the first row and first and second columns
print(A[0][0:2])

# Access the element on the first and second rows and third column
print(A[0:2, 2])


# Addition
# Create a numpy array X
X = np.array([[1, 0], [0, 1]])
print(X)
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]])
print(Y)
# Add X and Y
Z = X + Y
print(Z)

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]])
print(Y)

# Multiply Y with 2
Z = 2 * Y
print(Z)

# Create a numpy array
Y = np.array([[2, 1], [1, 2]])
print(Y)

# Create a numpy array
X = np.array([[1, 0], [0, 1]])
print(X)

# Multiply X with Y
Z = X * Y
print(Z)

# Muptiply like algebra
# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
print(A)
# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
print(B)
# Calculate the dot product
Z = np.dot(A, B)
print(Z)
# Calculate the sine of Z
print(np.sin(Z))

# Create a matrix C
C = np.array([[1, 1], [2, 2], [3, 3]])
print(C)
# Get the transposed of C
print(C.T)

# convert it to numpy array
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
arr = np.array(a)
print(a)

# calculate the numpy array size
print(arr.size)

# access the element on the first row and first and second column
print(arr[0][0:2])

# perform matrix multiplication with the numpy arrays A and B
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
X = np.dot(arr, B)
print(X)