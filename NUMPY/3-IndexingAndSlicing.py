# Indexing and Slicing in NumPy Refers to selecting of a subset of elements from a sequence of numbers. 
# It is a way of accessing a subset of elements from a larger sequence of numbers. 
# In Python, indexing and slicing can be done using square brackets [] and the colon : operator.
# Indexing and slicing in NumPy is similar to indexing and slicing in Python lists, but it is more powerful and efficient. 
# In NumPy, indexing and slicing can be done using square brackets [] and the colon : operator.
# Indexing and slicing in NumPy is used to access and manipulate the elements of a NumPy array.
import numpy as np
# Indexing and slicing in NumPy is used to access and manipulate the elements of a NumPy array.
# Indexing in NumPy is used to access a single element of a NumPy array.
# Slicing in NumPy is used to access a subset of elements from a NumPy array
# Indexing in NumPy is done using square brackets [] and the index of the element to be accessed.
# Slicing in NumPy is done using square brackets [] and the colon : operator.
# Syntact for indexing and slicing in NumPy is as follows:
# array[start:stop:step] # 1d array
# array[:,start:stop:step] # 2d array ans so on
# where start is the index of the first element to be accessed, stop is the index of the last element to be accessed, and step is the number of elements to be skipped.
# NOTE: That the start index is inclusive and the stop index is exclusive.
# If start is not specified, it defaults to 0. If stop is not specified, it defaults to the length of the array.
# If step is not specified, it defaults to 1.
# Here are some examples of indexing and slicing in NumPy:
# 1. Indexing in NumPy
array = np.array([1, 2, 3, 4, 5])
# Accessing the first element of the array
print(array[0])  # Output: 1

# Some Examples of Slicing in NumPy:
# 2. Slicing in NumPy
print(array[1:4])  # Output: [2 3 4] (elements from index 1 to 3)
print(array[:3])   # Output: [1 2 3] (elements from index 0 to 2)
print(array[2:])   # Output: [3 4 5] (elements from index 2 to the end)
print(array[::2])  # Output: [1 3 5] (every second element)
print(array[::-1]) # Output: [5 4 3 2 1] (reversed array)

# 3. Fancy Indexing in NumPy
# Fancy indexing allows you to access multiple elements of an array using a list or array of indices.
# It is useful when you want to access non-contiguous elements of an array.
# Example of fancy indexing:
print(array[[0, 2, 4]])  # Output: [1 3 5] (accessing elements at indices 0, 2, and 4)

# 4. Boolean Masking in NumPy
# Boolean masking allows you to access elements of an array based on a condition.
# example of boolean masking:
print(array[array > 2])  # Output: [3 4 5] (accessing elements greater than 2)