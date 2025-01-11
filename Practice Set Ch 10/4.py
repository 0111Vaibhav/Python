# Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self,number):
        square = number * number
        cube = number ** 3
        squareroot = number ** 0.5
        print(f'''square, cube and square root of a number is : 
Square = {square}
Cube = {cube}
squareroot = {squareroot}''')
    def greet(self):
        print("Good Morning")

cal = Calculator(25)
cal.greet()