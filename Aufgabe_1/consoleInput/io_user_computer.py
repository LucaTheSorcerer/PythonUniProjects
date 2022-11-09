import random

def user_input():
    user_action = input("Enter a choice --> rock, paper, scissors: ")
    return user_action
input_from_user = user_input()
#print(f"Input from user is {input_from_user}")

def computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action
input_from_computer = computer_choice()
print(f"Input from computer is {input_from_computer}")

