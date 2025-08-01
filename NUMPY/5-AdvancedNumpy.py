# Array Modification
# you can insert, delete, or append elements to an array.
# The `insert()`, `delete()`, and `append()` methods are used for these
# They create new arrays with the specified modifications.
# 2. Inserting Elements
# The `insert()` method is used to insert elements into an array at a specified index.
# syntax: `numpy.insert(array, index, values, axis=None)`,
# where `array` is the original array, `index` is the position where the new values should be inserted,
# `values` is the value(s) to be inserted, and `axis` specifies the axis along which to insert the values i.e Rows and Collumns.
# Example of inserting an element into an array:
import numpy as np
# Create an array
array = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(array)
# Insert an element at index 2
inserted_array = np.insert(array, 2, 10)
print("Array after inserting 10 at index 2:")
print(inserted_array)  # Output: [ 1  2 10  3  4  5]
# insert() in a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D Array:")
print(array_2d)
# Insert a row at index 1
inserted_row = np.insert(array_2d, 1, [7, 8, 9], axis=0)
print("2D Array after inserting a row at index 1:")
print(inserted_row)  # Output: [[1 2 3] [7 8 9] [4 5 6]]

# 2. Appending Elements
# The `append()` method is used to add elements to the end of an array.
# syntax: `numpy.append(array, values, axis=None)`,
# where `array` is the original array, `values` is the value(s) to be appended,
# and `axis` specifies the axis along which to append the values.
# Example of appending an element to an array:
array = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(array)
# Append an element to the end of the array
appended_array = np.append(array, 6)
print("Array after appending 6:")
print(appended_array)  # Output: [1 2 3 4 5 6]
# Append a row to a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D Array:")
print(array_2d)
# Append a row to the end of the 2D array
appended_row = np.append(array_2d, [[7, 8, 9]], axis=0)
print("2D Array after appending a row:")
print(appended_row)  # Output: [[1 2 3] [4 5 6] [7 8 9]]

# 3. Concatenating Arrays
# The `concatenate()` method is used to join two or more arrays along a specified axis
# syntax: `numpy.concatenate((array1, array2, ...), axis=0)`,
# where `array1`, `array2`, etc. are the arrays to be concatenated, and `axis` specifies the axis along which to concatenate.
# Example of concatenating two arrays:
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
# Concatenate the two arrays along axis 0 (default)
concatenated_array = np.concatenate((array1, array2))
print("Concatenated Array:")
print(concatenated_array)  # Output: [1 2 3 4 5 6]
# Concatenate two 2D arrays along axis 0
array1_2d = np.array([[1, 2, 3], [4, 5, 6]])
array2_2d = np.array([[7, 8, 9], [10, 11, 12]])
print("2D Array 1:")
print(array1_2d)
print("2D Array 2:")
print(array2_2d)
# Concatenate the two 2D arrays along axis 1
concatenated_2d = np.concatenate((array1_2d, array2_2d), axis=1)
print("Concatenated 2D Array:")
print(concatenated_2d)  # Output: [[ 1  2  3  7  8  9] [ 4  5  6 10 11 12]]
# axis=1 means Horizontal stacking, axis=0 means Vertical stacking

# 4. Deleting Elements
# The `delete()` method is used to remove elements from an array at a specified index.
# syntax: `numpy.delete(array, index, axis=None)`,
# where `array` is the original array, `index` is the position of the element(s) to be deleted,
# and `axis` specifies the axis along which to delete the elements.
# Example of deleting an element from an array:
array = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(array)
# Delete the element at index 2
deleted_array = np.delete(array, 2, axis=0)
print("Array after deleting the element at index 2:")
print(deleted_array)  # Output: [1 2 4 5]
# Delete a row from a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:")
print(array_2d)
# Delete the row at index 1
deleted_row = np.delete(array_2d, 1, axis=0)
print("2D Array after deleting the row at index 1:")
print(deleted_row)  # Output: [[1 2 3] [7 8 9]]

# 5. Stacking Arrays
# Stacking arrays allows you to combine multiple arrays into a single array along a specified axis.
# The `hstack()` method is used for horizontal stacking, and the `vstack()` method is used for vertical stacking.
# Example of horizontal stacking:
# Horizontal stacking combines arrays side by side (along columns).
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
# Horizontal stacking of two arrays
hstacked_array = np.hstack((array1, array2))
print("Horizontally Stacked Array:")
print(hstacked_array)  # Output: [[1 2 5 6] [3 4 7 8]]
# Example of vertical stacking:
# Vertical stacking combines arrays one on top of the other (along rows).
# Vertical stacking of two arrays
vstacked_array = np.vstack((array1, array2))
print("Vertically Stacked Array:")
print(vstacked_array)  # Output: [[1 2] [3 4] [5 6] [7 8]]
# Note: The main difference between concatenation and stacking is that stacking creates a new dimension,
# while concatenation combines arrays along an existing dimension. 

# 6. Splitting Arrays
# Splitting arrays allows you to divide an array into multiple sub-arrays.
# The `split()` method is used to split an array into multiple sub-arrays along a specified axis.
# syntax: `numpy.split(array, indices_or_sections, axis=0)`,
# where `array` is the original array, `indices_or_sections` specifies the indices or sections to split the array,
# and `axis` specifies the axis along which to split the array.
# Example of splitting an array:
array = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(array)
# Split the array into 3 equal parts
split_arrays = np.split(array,3) # Output: (array([1, 2]), array([3, 4]), array([5, 6]))
print("Split Arrays:")
print(split_arrays)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]
# Split a 2D array into two parts along axis 0
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Original 2D Array:")
print(array_2d)
# Split the 2D array into two parts along axis 0
split_2d_arrays = np.split(array_2d, 2, axis=0)
print("Split 2D Arrays:")
print(split_2d_arrays)  # Output: [array([[1, 2, 3], [4, 5, 6]]), array([[7, 8, 9], [10, 11, 12]])]
# Split a 2D array into two parts along axis 1
split_2d_arrays_axis1 = np.split(array_2d, 3, axis=1)
print("Split 2D Arrays along axis 1:")
print(split_2d_arrays_axis1)  # Output: [array([[1], [4], [7], [10]]), array([[2], [5], [8], [11]]), array([[3], [6], [9], [12]])]

