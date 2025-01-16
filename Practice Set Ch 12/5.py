# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

# Define a list of numbers from 1 to 10
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Prompt the user to input a number
# This number will be used to generate a multiplication table
n = int(input("Enter a Number : "))

# Use a list comprehension to create the multiplication table
# For each number 'i' in the list 'l', calculate 'n × i' and format it as a string
# Example: If n = 3 and i = 4, the formatted string will be "3 × 4 = 12"
tl = [f"{n} × {i} = {n*i}" for i in l]

# Open a file with the name "<n>.txt" in write mode ('w')
# Example: If n = 5, the file will be named "5.txt"
with open(f"Practice Set Ch 12/{n}.txt", "w") as f:
    # Iterate through the list of formatted strings (tl)
    for i in tl:
        # Write each string to the file, followed by a newline character ('\n')
        f.write(f"{i}\n")

# Sample Output for the file named "5.txt" when n = 5:
# 5 × 1 = 5
# 5 × 2 = 10
# 5 × 3 = 15
# 5 × 4 = 20
# 5 × 5 = 25
# 5 × 6 = 30
# 5 × 7 = 35
# 5 × 8 = 40
# 5 × 9 = 45
# 5 × 10 = 50

# Alternative (commented out for reference):
# Write the table to a file named "tables.txt" in append mode ('a')
# This adds the table to the file without overwriting existing content
# with open("tables.txt", "a") as f:
#     f.write(f"Table of {n}: {str(table)} \n")

# Sample Output for appending the table in "tables.txt" when n = 5:
# Table of 5: ['5 × 1 = 5', '5 × 2 = 10', '5 × 3 = 15', '5 × 4 = 20', '5 × 5 = 25', 
#              '5 × 6 = 30', '5 × 7 = 35', '5 × 8 = 40', '5 × 9 = 45', '5 × 10 = 50']
