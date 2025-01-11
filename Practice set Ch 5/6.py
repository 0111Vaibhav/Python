
# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d={}
f1=input("Enter Your Name : ")
l1=input("Enter Your fav Language : ")
f2=input("Enter Your Name : ")
l2=input("Enter Your fav Language : ")
f3=input("Enter Your Name : ")
l3=input("Enter Your fav Language : ")
f4=input("Enter Your Name : ")
l4=input("Enter Your fav Language : ")

d.update({f1:l1,
          f2:l2,
          f3:l3,
          f4:l4
          })
print(d)