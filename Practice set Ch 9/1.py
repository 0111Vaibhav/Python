
# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

f = open("Practice set Ch 9/poems.txt")
text =  f.read()
if( "twinkle" in text):
    print("The File Contains the string \"twinkle\"")
else:
    print("The File does not Contain the string \"twinkle\"")
f.close()

