
# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score.

import random as r
def game():
    print("You are Playing a game...")
    score=r.randint(1,100)
    with open("Practice set Ch 9/Hi-score.txt") as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = 0
        else:
            hiscore = int(hiscore)
    
    print(f"Your Score = {score}")
    if(score > hiscore):
        with open("Practice set Ch 9/Hi-score.txt", "w") as f:
            f.write(str(score))
    return score

game()