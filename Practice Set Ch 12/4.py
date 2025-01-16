# Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.

# Prompt the user to input the first number
# The input is converted to an integer using int()
a = int(input("Enter a Number : "))

# Prompt the user to input the second number
# This will also be converted to an integer
b = int(input("Enter another Number : "))

# Use a try-except block to handle potential errors during division
try:
    # Attempt to divide 'a' by 'b' and print the result
    # f-strings are used to format the output
    print(f"Number {a} divided by Number {b} is {a/b}")
except ZeroDivisionError:
    # If a division by zero occurs, this block is executed
    # Print the symbol for infinity (∞) to represent the result
    print("∞")
   
