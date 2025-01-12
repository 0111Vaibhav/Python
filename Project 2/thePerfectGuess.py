# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number.

# Importing the random module with alias 'r' for generating random numbers
import random as r

# Prompting the user to guess a number
print("Guess a Number between 1 and 100")

# Generating a random number between 1 and 100
randomNum = r.randint(1, 100)

# Initializing the count for the number of guesses made by the user
guessCount = 1

# Initializing inputNum with a value that won't match the random number initially
inputNum = -1

# Starting a loop that continues until the user guesses the correct number
while inputNum != randomNum:

    try:
        # Asking the user to guess a number and converting the input to an integer
        inputNum = int(input("Guess The Number : "))
        
        # Checking if the guessed number is greater than the random number
        if inputNum > randomNum:
            print("Lower number please")  # Hint to guess a smaller number
            guessCount += 1  # Incrementing the guess count
        
        # Checking if the guessed number is less than the random number
        elif inputNum < randomNum:
            print("Higher number please")  # Hint to guess a larger number
            guessCount += 1  # Incrementing the guess count
        
        # Checking if the guessed number is out of the valid range (1 to 100)
        elif inputNum > 100 or inputNum < 1:
            # Raising an exception if the input is outside the valid range
            raise ValueError("You Have to Enter a number Between 1 and 100")   
    
    # Handling invalid input or value errors (e.g., non-integer input)
    except ValueError:
        print("Enter a Valid Integer Number")  # Prompting the user to enter a valid number

# Executing this block if the guessed number matches the random number
if inputNum == randomNum:
    # Congratulating the user and displaying the number of attempts made
    print(f"You Have Correctly Guessed the Number : {randomNum} in {guessCount} Guesses")
