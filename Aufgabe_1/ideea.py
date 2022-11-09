import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def selection_from_user():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    #user_input = input("Enter a choice (rock[0], paper[1], scisors[2]")
    #selection = int(user_input)
    action = Action(selection)
    return Action
selection_from_user()

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action
print(get_computer_selection())

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It is a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts Paper! You win")
        else:
            print("Rock destroys scissors! You lose!")


gamenumber = 0
playerscore = 0
computerscore = 0
while gamenumber < 3:
    try:
        user_action = selection_from_user()
    except ValueError as e:
        range_str = f"[0, {len(Action)-1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)




