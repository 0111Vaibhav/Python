
# Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * * 

n=int(input("Enter a number: "))
for i in range(n):
    if i == 0 or i == n - 1:  # First and last rows
        print('* ' * n)
    else:  # Middle rows
        print('* ' + '  ' * (n - 2) + '*')
print("End of Loop")