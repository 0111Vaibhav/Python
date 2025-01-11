
# Write a program to find out the line number where python is present from ques 6.

lineNo = 1
with open("Practice set Ch 9/log.txt") as f:
    content = f.readlines()
for line in content:
    if("Python" in line):
        print(f"Line number {lineNo} contains \"Python\" String")
        break
    else:
        lineNo += 1
                
