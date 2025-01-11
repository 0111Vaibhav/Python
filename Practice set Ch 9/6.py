
# Write a program to mine a log file and find out whether it contains ‘python’.

with open("Practice set Ch 9/log.txt") as f:
    content = f.read()

if ("Python" in content):
    print("File Contains \"Python\" string.")
else:
    print("File does not contain \"Python\" string.")

    