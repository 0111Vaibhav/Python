
# Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1,+1):
    sum+=i
print(sum)