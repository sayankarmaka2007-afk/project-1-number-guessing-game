# Number Guessing Game

import random
secret_number= random.randint(1,100)
tries=0
while tries<7:
    guess=int(input("Enter a number between 1 and 100:"))
    tries+=1
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print ("Too high")
    else:
        print("you guess the correct number")
        break
else:
    print(" You has used your 7 tries")
    print("The secret number:", secret_number)
