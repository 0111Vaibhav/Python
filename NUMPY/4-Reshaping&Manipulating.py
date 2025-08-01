# Reshaping and Manipulating Arrays
import numpy as np
# Reshaping and manipulating arrays in NumPy allows you to change the shape, size, and structure of arrays.
# This is useful when you want to prepare data for analysis or when you want to change the way data is organized.
# Here are some common operations for reshaping and manipulating arrays in NumPy:
# 1. Reshaping Arrays
# Reshaping allows you to change the shape of an array without changing its data.
# The `reshape()` method is used to change the shape of an array.
# The new shape must have the same number of elements as the original array.
# Example of reshaping an array:
array = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(array)
# Reshaping the array to have 3 rows and 2 columns
reshaped_array = array.reshape(3, 2)
print("Reshaped Array (3 rows, 2 columns):")
print(reshaped_array)

# Ravel and Flattening Arrays
# The `ravel()` method returns a flattened version of the array, which is a 1D array containing all elements.
# The `flatten()` method also returns a flattened version of the array, but it returns a copy of the original array.
# Difference between `ravel()` and `flatten()`:
# - `ravel()` returns a flattened view of the original array, while `flatten()` returns a copy.
# - If the original array is modified, the changes will be reflected in the view returned by `ravel()`, but not in the copy returned by `flatten()`.
print("Ravelled Array:")
print(array.ravel())  # Output: [1 2 3 4 5 6]
print("Flattened Array:")
print(array.flatten())  # Output: [1 2 3 4 5 6]

