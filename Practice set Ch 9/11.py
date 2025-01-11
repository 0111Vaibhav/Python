
# Write a python program to rename a file to “renamed_by_ python.txt.

with open("Practice set Ch 9/file.txt") as f:
    content = f.read()

with open("Practice set Ch 9/renamed_by_ python.txt","w") as f:
    f.write(content)