import random

def user_input():
    user_action = input("Enter a choice --> rock, paper, scissors: ")
    return user_action
print(user_input())

def computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action
print(computer_choice())

