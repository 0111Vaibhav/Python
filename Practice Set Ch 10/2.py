# Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class Calculator:
    def __init__(self,number):
        square = number * number
        cube = number ** 3
        squareroot = number ** 0.5
        print(f'''square, cube and square root of a number is : 
Square = {square}
Cube = {cube}
squareroot = {squareroot}''')

cal = Calculator(25)
        
        