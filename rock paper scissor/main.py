import random
from ascii import *

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice > 2:
    print("You have chosen incorrectly, you lost!")
else:
    options = [rock, paper, scissor]

    print(options[user_choice])
    print("Computer Chose:")
    print(options[computer_choice])

    if user_choice + 1 == computer_choice or user_choice - 2 == computer_choice:
        print("You Lost!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You Win!")
