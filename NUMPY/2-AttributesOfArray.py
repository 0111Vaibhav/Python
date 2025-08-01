# Attributes of array in Numpy 
# An array in Numpy has various attriutes which can be accessed using dot notation.
# They help us in understanding the array and its properties while performing Calculation on Large amount of Data
import numpy as np
# Here are some of the attributes of array in Numpy


# 1. shape
array = np.array([[1, 2, 3, 4, 5],
                 [5, 6, 7, 8, 9]])
print(array.shape)  # Output: (2, 5) Where 2 is the number of rows and 5 is the number of columns

# 2. size
print(array.size)  # Output: 10 Where 10 is the total number of elements in the array

# 3. dimension
print(array.ndim) # Output: 2 Where 2 is the number of dimensions in the array

# 4. datatype
print(array.dtype) # Output: int64 Where int64 is the data type of the array

# 5. astype , It Changes the type of the array elements
floatArray= array.astype('float64')  
print(floatArray) # Output: [[1. 2. 3. 4. 5.] [5. 6. 7. 8. 9.]]
print(floatArray.dtype) # Output: float64

# 6. operators
# Numpy arrays support various operators like +, -, *, /, %, **, // etc. These operators are used to perform element-wise operations on the arrays.
# For example, if we have two arrays, a and b, then a + b will add
# corresponding elements of a and b and return a new array with the result.
# Here is an example of using operators on Numpy arrays.
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 6, 7, 8, 9])
# Addition of two arrays
print(array1 + array2)  # Output: [6 8 10 12 14]

# 7. aggrigate functions 
# Numpy arrays support various aggregate functions like sum, mean, median, max, min, std, var
# These functions are used to calculate the aggregate value of the array elements.
# For example, if we have an array, then np.sum() will return the sum of all elements in the array.
# Here is an example of using aggregate functions on Numpy arrays.
array7 = np.array([1, 2, 3, 4, 5])
# Sum of all elements in the array
print(np.sum(array7))  # Output: 15
# Mean of all elements in the array
print(np.mean(array7))  # Output: 3.0
# Median of all elements in the array
print(np.median(array7))  # Output: 3.0
# Maximum value in the array
print(np.max(array7))  # Output: 5
# Minimum value in the array
print(np.min(array7))  # Output: 1
# Standard Deviation of all elements in the array
print(np.std(array7))  # Output: 1.4142135623730951
# Varience of all elements in the array
print(np.var(array7))  # Output: 2.0

