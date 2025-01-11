# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Calculator:
    def __init__(slf,number):
        square = number * number
        cube = number ** 3
        squareroot = number ** 0.5
        print(f'''square, cube and square root of a number is : 
Square = {square}
Cube = {cube}
squareroot = {squareroot}''')

cal = Calculator(25)

# Ans: Yes you can and it does not affect the code