from playsound import playsound
import PyObjCTools
import cv2
import numpy as np
import random
from Aufgabe_1.read_from_files.read_lines import *
from Aufgabe_1.game_logic.logic import *
from Aufgabe_1.data.data import *

def play_videoFile(filePath, mirror=False):
    cap = cv2.VideoCapture("Aufgabe_1/YOU_DIED.mp4")
def playGame():
    """
    This function contains the code for taking input and output and then playing the game, at the end
    comparing the value and printing it prints the possible result from the dictionary results based on the function
    Logic Game
    :return:
    """
    options = ("Rock", "Paper", "Scissors")  # This tuple stores all the options for the game

    results = {1: "You win!", 2: "Computer wins!", 3: "It's a tie!"}  # This dictionary stores the all the possible outputs

    cscore = 0
    pscore = 0
    gamen = 0

    while gamen < 3:  # While the number of games is <3 the game will keep going
        print(f"Your score is {pscore}")
        print(f"The computer's score is {cscore}")
        choices()

        playerOption = int(input("Your choice for the game ").strip())
        if playerOption == 1:
            read_lines_for_rock()
            # print_rock()
        elif playerOption == 2:
            read_lines_for_paper()
            # print_paper()
        elif playerOption == 3:
            read_lines_for_scissors()
            # print_scissors()

        if playerOption not in range(1, 4):
            print("Invalid Option")
            continue


        computerOption = random.choice(options)
        print(f"The computer chose {computerOption}")

        computerOption = options.index(computerOption) + 1

        if computerOption == 1:
            read_lines_for_rock()

        elif computerOption == 2:
            read_lines_for_paper()
        elif computerOption == 3:
            read_lines_for_scissors()

        result = logicGame(playerOption, computerOption)

        print(results[result])

        if result == 1:
            pscore += 1
            gamen += 1
        elif result == 2:
            cscore += 1
            gamen += 1

    if cscore > pscore:
        print("The computer destroyed you. Press F to pay respects 💀")
    else:
        print("You defeated the machine! Well done, you stopped them from taking over! 🎉")
        playsound("Aufgabe_1/mlg.mp3")