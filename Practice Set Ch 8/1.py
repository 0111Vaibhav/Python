
# Write a program using functions to find greatest of three numbers

def Max(a,b,c):
    if(a>b and a>c):
        print(f"{a} is Maximum number")
    elif(b>a and b>c):
        print(f"{b} is Maximum number")
    elif(c>a and c>b):
        print(f"{c} is Maximum number")
x=int(input("Enter a no. : "))
y=int(input("Enter a no. : "))
z=int(input("Enter a no. : "))
Max(x,y,z)
    