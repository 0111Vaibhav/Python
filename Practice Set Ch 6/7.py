
# Write a program to find out whether a given post is talking about “Harry” or not

p=input("Enter a Post : ")
if("Harry".lower in p.lower):
    print("post is not talking about “Harry”")
else:
    print("post is talking about “Harry”")