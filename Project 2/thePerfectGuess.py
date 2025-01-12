# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number.

import random as r

print("Guess a Number between 1 and 100")
randomNum = r.randint(1,100)
guessCount = 1
inputNum = -1
while( inputNum != randomNum ):

    try:
        inputNum = int(input("Guess The Number : "))
    
        if( inputNum > randomNum ):
            print("Lower number please")
            guessCount += 1
        
        elif( inputNum < randomNum ):
            print("Higher number please")
            guessCount += 1
        
        elif( inputNum > 100 or inputNum < 1 ):
            raise ValueError("You Have to Enter a number Between 1 and 100")   
    
    except ValueError:
        print("Enter a Valid Integer Number")


if( inputNum == randomNum ):
    print(f"You Have Correctly Guessed the Number : {randomNum} in {guessCount} Guesses")