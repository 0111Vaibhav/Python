# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.

with open("Practice set Ch 9/file.txt") as f:
    content = f.read()
    newContent = content.replace("donkey","#####")
with open("Practice set Ch 9/file.txt","w") as f:
    f.write(newContent)
