import random
def random_number():
    Rnumber = random.randint(1,100)
    attempt =0
    try:
        while True:
            number = int(input("enter your number between 1 to 100: " ))
            attempt = attempt+1
            if(number<Rnumber):
                print("your no. is less then random no.!!!!")
            elif(number>Rnumber):
                print("your no. is more then random no.!!!!")
            else:
                print("thik hai bhai!!! has lee!!!! vese bhi itna hi ata he.....")
                break
    except ValueError:
        print("enter valid number") 
while True:
    random_number()
    choice = input("do you want to play again? to bhai khel lenaaaaaa!!!! to bhai yes likhna")   

    if(choice == "yes"):
        random_number()   
    else:
        break   