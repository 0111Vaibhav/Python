# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

g = int(input("Enter Grade : "))
if(g>90 and g<=100):
    print("Grade Is Ex")
elif(g>80 and g<=90):
    print("Grade is A")
elif(g>70 and g<=80):
    print("Grade is B")
elif(g>60 and g<=70):
    print("Grade is C")
elif(g>=50 and g<=60):
    print("Grade is D")
else:
    print("Grade is F")