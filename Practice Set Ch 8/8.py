
# Write a python function to print multiplication table of a given number

def table(n):
    for i in range(1,11,+1):
        print(f"{n} × {i} = {n*i}")
a=int(input("Enter a number: "))
table(a)