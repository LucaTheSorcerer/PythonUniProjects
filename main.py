from Aufgabe_1.main import playGame
from Aufgabe_2.main import changeWords_to_call_WordsChange
from Aufgabe_3.write_turtle import writeToTurtle
"""
This file binds all the exercises together so that the user can call them directly from the terminal 
"""

exercises = {
    "1": playGame,
    "2": changeWords_to_call_WordsChange,
    "3": writeToTurtle
}

def printOptions():
    print("1. Play Rock Paper Scissors!")
    print("2. Change your words!")
    print("3. Draw letter!")
    print("If the input is an invalid input, the program will stop! ")

def run_program():

    while True:
        printOptions()

        option = input("Choose your option to run different programs: ").strip()

        if option in exercises:
            exercises[option]()
        else:
            print("Not a valid option")
            break
run_program()

