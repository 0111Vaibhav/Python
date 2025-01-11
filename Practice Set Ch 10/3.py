# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?
class Class:
    a="Class Attribute"

o = Class()
o.a = "Object Attribute"

print(o.a)
print(Class.a) 
#Ans : No It does not Class attribute and object attribute are both different