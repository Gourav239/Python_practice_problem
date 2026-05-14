import random
i=1

while i:
    genNum=random.randint(1,15)

    userNum=int(input("Enter number between 1 to 15 : "))

    if(genNum==userNum) :
        print("You guessed it right!")
        i=0
    else: 
        print("Better Luck next time")   
    i=int(input("Press 0 to exit , else any number except 0 : "))    
