
# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the
# user.

import random
'''
"Snake" = 1
"Gun" = -1
"Water" = 0
'''
computer = random.choice([-1,0,1])
yourInptStr =input("Enter Your chocie : ")
youDict = {
    "s" :  1,
    "S" :  1,
    "g" : -1,
    "G" : -1,
    "w" :  0,
    "W" :  0
}
you = youDict[ yourInptStr ]
revDict = {
    1 : "Snake",
    -1 : "Gun",
    0 : "Water"
}
print(f"Your Choice is {revDict[you]}\nComputer Choosed {revDict[computer]}, Therefore")
if(you == computer):
    print("Its a Draw")
else:
    if(computer == -1 and you == 0):
        print("You Win!")
    elif(computer == -1 and you == 1):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Lose!")
    elif(computer == 0 and you == -1):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Win!")
    else:
        print("Something went Wrong")
    