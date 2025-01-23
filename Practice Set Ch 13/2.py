# print("{} is a {} boy".format("Vaibhav","good")) >> Example for using Format

# Write a program to input name, marks and phone number of a student and format it 
# using the format function like below: 
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = str(input("Enter Your Name : "))
marks = int(input("Enter Your Marks : "))
mobileNo = int(input("Enter Your Mobile num : "))

print("The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,mobileNo))