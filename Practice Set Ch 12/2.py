# Write a program to print third, fifth and seventh element from a list using enumerate 
# function.

# Define a list of numbers
l = [1, 2, 3, 4, 5, 6, 7]

# Use enumerate to iterate through the list with indices starting at 1
# enumerate() generates pairs of (index, element) for each item in the list
# 'start=1' makes the index start from 1 instead of the default 0
for index, e in enumerate(l, start=1):
    # Check if the current index matches 3, 5, or 7
    # The condition filters only the specified indices
    if index == 3 or index == 5 or index == 7:
        # Print the index and the corresponding element
        # f-strings are used for clean, formatted output
        print(f"Index : {index}, Element : {e}")
