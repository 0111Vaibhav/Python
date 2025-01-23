# Write a program to find the maximum of the numbers in a list using the reduce 
# function.

list = [10,1,2,5,40,80,41,52]
from functools import reduce
max = reduce(lambda x,y:max(x,y),list)
print(max) 
