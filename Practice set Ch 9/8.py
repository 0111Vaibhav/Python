
# Write a program to make a copy of a text file “this. txt” 

with open("Practice set Ch 9/this.txt") as f:
    content = f.read()
with open("Practice set Ch 9/thisCopy.txt","w") as f:
    f.write(content)
    