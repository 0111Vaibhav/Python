
# Write a python function which converts inches to cms

def convert(inches):
    cm = inches*2.54
    return cm
i=int(input("Enter inches : "))
print(convert(i))