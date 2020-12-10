#EXERCISE 4
#Exercise Number gussing game
# make a varible , like winning_number and assing by number to it.
# Ask user to guess a number
# if user guessed correctly then print "You Win !!!!"
#if user don`t guessed correctly then:
#If user guessed lower then actual number then print "Too Low"
#If user gussed higher then actual number then print "Too High"

# winning_number = 25
# user_input = int(input("Guess a number = "))
# if user_input == winning_number:
#     print("YOU WIN !!!!")
# else:
#     if user_input< winning_number:
#         print("TOO LOW !!!")
#     else:
#         print("TOO HIGH !!")


#===============================================================
# Modify Number Guessing Game.

import random
winning_number = random.randint(1,100)
guess = 1
user_input = int(input("Guess a number = "))
game_over = False
while not game_over:
    if user_input == winning_number:
        print(f"YOU WIN !!!!, and you guess this number in {guess} time")
        game_over = True
    else:
        if user_input< winning_number:
            print("TOO LOW !!!")
            guess += 1
            user_input = int(input("Guess this number again : "))
        elif user_input>winning_number:
            print("TOO HIGH !!")
            guess += 1
            user_input = int(input("Guess this number again : "))

#####===========================================
# Number Guessing Game

# print(" This is a number guessing game ")
# import random
# random_number = random.randrange(1,100)
# guess= int(input("What could be the number ? : "))
# correct = False
# print(random_number)
# while not correct:
#     if guess == random_number:
#         print("Congrats You got it")
#         correct =True
#     elif guess>random_number:
#         print("Too High")
#         break
#     elif guess<random_number:
#         print("Too Low")
#         break
#     else:
#         print("Try somthing else :")
       