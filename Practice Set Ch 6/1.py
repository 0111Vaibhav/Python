
# Write a program to find the greatest of four numbers entered by the user

n1= int(input("Enter Num 1: "))
n2= int(input("Enter Num 2: "))
n3= int(input("Enter Num 3: "))
n4= int(input("Enter Num 4: "))
if(n1>n2):
    if(n1>n3):
        if(n1>n4):
            print(n1," is Max")
        else:
            print(n4," is Max")
    else:
        if(n3>n4):
            print(n3," is Max")
        else:
            print(n4," is Max")
else:
    if(n2>n3):
        if(n2>n4):
            print(n2," is Max")
        else:
            print(n4," is Max")
    else:
        if(n3>n4):
            print(n3," is Max")
        else:
            print(n4," is Max")