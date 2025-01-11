
# Write a program to find whether a given number is prime or not.

n=int(input("Enter a number: "))
if(n==2):
    print("Entered number is not a Prime number")
else:
    for i in range(2,n):
        if(n%i==0):
            print("Entered number is not a Prime number")
            break
        else:
            print("Entered number is a Prime number")
            break
    print("End of Loop")
    
