# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same.

try:
    # Attempt to open three files simultaneously using the 'with' statement
    # '1.txt', '2.txt', and '3.txt' are the file names
    with open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3:
        # Placeholder 'pass' means no action is taken here for now
        pass
except FileNotFoundError:
    # If any of the specified files are not found, this block is executed
    print("File Not Found")  # Print a message indicating the missing file
 
    