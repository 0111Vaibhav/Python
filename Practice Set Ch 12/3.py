# Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 

# Define a list of numbers from 1 to 10
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ask the user to input a number to generate its multiplication table
# The input is converted to an integer using int()
n = int(input("Enter a Number : "))

# Use a list comprehension to create a multiplication table
# For each number 'i' in the list 'l', calculate 'n × i' and format it as a string
# Example: If n = 2 and i = 3, the formatted string will be "2 × 3 = 6"
tl = [f"{n} × {i} = {n*i}" for i in l]  # Alternatively, we could use range(1, 11) instead of 'l'

# Print the resulting list of formatted multiplication table strings
print(tl)
