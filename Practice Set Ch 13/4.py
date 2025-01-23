# Write a program to filter a list of numbers which are divisible by 5.

def divisibleByFive(n):
    if n%5==0:
        return True
    return False

l = [2,5,7,10,15,17,200,18,20,25,36]
print(list(filter(divisibleByFive,l)))
