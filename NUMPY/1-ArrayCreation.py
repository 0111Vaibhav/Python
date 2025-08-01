# Creating Arrays from List in numpy
# We can create an array from a list using the numpy.array(list) function.
# This function takes a list as an argument and returns a numpy array.
import numpy as np
# Creating a list
l1 = [1,2,3,4]
# Creating a numpy array from the list
arr = np.array(l1)
# Printing the numpy array
print(arr)  # Output: [1 2 3 4]



#We can also Create arrays with default values
# We can create an array with default values using the numpy.zeroes((shape)) function.
# This function takes the size of the array as an argument and returns an array with all elements as the default value (0 by default).
# Creating an array with default values
arrWithDefaultValues = np.zeros((3,3))
# Printing the array
print(arrWithDefaultValues)  
#  Output: 
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]



# We can also create arrays with default values using the numpy.full((shape),value) function.
# Creating an array with default value as 7
arrWithSetDefaultValue = np.full((3,3), 7)
# Printing the array
print(arrWithSetDefaultValue)  
#  Output: 
# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]



# We can also create sequences of numbers in NumPy
# We can create a sequence of numbers using the numpy.arange(start,stop,step) function.
# This function takes the start, stop and step values as arguments and returns an array of numbers from start to stop with a step size of step. 
# Creating a sequence of numbers from 1 to 10 with a step size of 2
arrSequence = np.arange(1,11,2)
# Printing the array
print(arrSequence)
# Output: [ 1  3  5  7  9]



# Creating Identity Matrix Using NumPy
# We can create an identity matrix using the numpy.eye(n) function.
# This function takes the size of the matrix as an argument and returns an identity matrix of that size.
# Creating an identity matrix of size 5x5
arrIdentity = np.eye(5)
# Printing the array
print(arrIdentity)
# Output: 
# [[1. 0. 0. 0. 0.] 
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

