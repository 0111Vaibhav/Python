
# Write a python program using function to convert Celsius to Fahrenheit.

def convert(celcuis):
    f = (celcuis * 9/5) + 32
    return f
c=int(input("Enter temperature in Celcuis :"))
print(convert(c))