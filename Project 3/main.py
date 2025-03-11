import random

name = input("What is your name? ")
print("Hello, " + name + "!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the characters: ")
guesses = ''
turns = 6
while(turns > 0):

    failed = 0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed+=1
            
    if(failed == 0):
        print("You Win!!!")
        print(f"The word is {word}")
        break
    
    guess = input("Guess the character:")
    guesses += guess
    
    if guess not in word:
        print("Wrong")
        turns -= 1
        print(f"You have {turns} more guesses left!!")
        
        if (turns == 0):
            print("Game Over......")             
    
