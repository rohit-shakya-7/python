# rock paper scissor :)

import random


# function to find out winner
def winner(pc, user):
    print("Your choice: {}".format(user))
    print("PC choice: {}".format(pc))
    if pc == user:
        print(f"Both players selected {pc}. It's a tie.")
    elif pc == "rock":
        if user == "paper":
            print("You won.")
        else:
            print("PC won.")
    elif pc == "scissors":
        if user == "rock":
            print("You won.")
        else:
            print("PC won.")
    else:
        if user == "scissors":
            print("You won.")
        else:
            print("PC won.")


# function to get input from the user
def choice():
    user_select = input("Enter your choice:")
    if user_select in possible_actions:
        return user_select
    print("Please type the valid word.")
    choice()


possible_actions = ["rock", "paper", "scissor"]
while True:
    print("Select your choice from the following: ")
    for i in possible_actions:
        print(i, end="\t")  # \t for printing the lists in same line
    print(); print("--------------")
    pc_selection = random.choice(possible_actions)  # random selection form the list.
    user_selection = choice()  # user input
    winner(pc_selection, user_selection)  # declaration of winner
    print()
    play_again = input("Play again? (y/n): ")   # text for playing again or not.
    print("--------------------------------------")
    print()
    if play_again != 'y':
        break
