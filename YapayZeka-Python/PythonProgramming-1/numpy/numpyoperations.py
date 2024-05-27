# Importing
import numpy as np

# Numpy basics
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15])  # 1*15 vector

print("Shape:", array.shape)

a = array.reshape(3, 5)
print("Shape:", a.shape)
print("Dimension:", a.ndim)

print("Data type:", a.dtype.name)
print("Size:", a.size)

print("Type:", type(a))

array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 5]])

zeros = np.zeros((3, 4))

zeros[0, 0] = 5
print(zeros)

np.ones((3, 4))

np.empty((2, 3))

a = np.arange(10, 50, 5)
print(a)

a = np.linspace(10, 50, 20)
print(a)

# Numpy basic operations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b:", a + b)
print("a - b:", a - b)
print("a squared:", a**2)

print("sin(a):", np.sin(a))

print("a < 2:", a < 2)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])

# Element-wise product
print("Element-wise product:", a * b)

# Matrix product
print("Matrix product:", a.dot(b.T))

print("Exponential of a:", np.exp(a))

a = np.random.random((5, 5))

print("Sum of all elements:", a.sum())
print("Maximum element:", a.max())
print("Minimum element:", a.min())

print("Sum along axis 0:", a.sum(axis=0))
print("Sum along axis 1:", a.sum(axis=1))

print("Square root of a:", np.sqrt(a))
print("Square of a:", np.square(a))  # a**2

print("Addition of a and a:", np.add(a, a))

# Indexing and slicing
array = np.array([1, 2, 3, 4, 5, 6, 7])  # Vector, dimension = 1

print("Element at index 0:", array[0])

print("Elements from index 0 to 3:", array[0:4])

reverse_array = array[::-1]
print("Reversed array:", reverse_array)

array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("Element at row 1, column 1:", array1[1, 1])

print("All elements in column 1:", array1[:, 1])

print("Elements in row 1, columns 1 to 3:", array1[1, 1:4])

print("Last row:", array1[-1, :])
print("Last column:", array1[:, -1])

# Shape manipulation
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Flatten
a = array.ravel()

array2 = a.reshape(3, 3)

arrayT = array2.T

print("Transpose shape:", arrayT.shape)

array5 = np.array([[1, 2], [3, 4], [4, 5]])

# Uncomment the line below if you want to stack arrays using column_stack
# array5 = np.column_stack((array1, array1))

# Stacking arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[-1, -2], [-3, -4]])

# Vertical stack
array3 = np.vstack((array1, array2))

# Horizontal stack
array4 = np.hstack((array1, array2))

# Convert and copy
liste = [1, 2, 3, 4]  # List

array = np.array(liste)  # Numpy array

liste2 = list(array)

a = np.array([1, 2, 3])


print("a", a)
b = a
print("b", b)
b[0] = 5
print("b", b)
c = a
print("c", c)

d = np.array([1, 2, 3])

e = d.copy()
print("e", e)
f = d.copy()
print("f", f)
