
# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n=int(input("Enter a number: "))
for i in range(1,n,+1):
    print(" "*(n-i),end="")
    print("*"*(i*2-1),end="")
    print("")
print("End of Loop")