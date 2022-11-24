from playsound import playsound
import PyObjCTools
import cv2
import numpy as np
import subprocess
import threading
import random
from Aufgabe_1.read_from_files.read_lines import *
from Aufgabe_1.game_logic.logic import *
from Aufgabe_1.data.data import *

# def play_videoFile():
#     cap = cv2.VideoCapture("Aufgabe_1/YOU_DIED.mp4")
#     ret, frame = cap.read()
#     if (cap.isOpened() == False):
#         print("Error opening file")
#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if ret == True:
#             cv2.imshow('Frame', frame)
#
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 break
#         else:
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
# play_videoFile()
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
            playsound("Aufgabe_1/bruh2.mp3")
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
        playsound("Aufgabe_1/lost.mp3")
        playsound("Aufgabe_1/stupid.mp3")
    else:
        print("You defeated the machine! Well done, you stopped them from taking over! 🎉")
        playsound("Aufgabe_1/mlg.mp3")
        playsound("Aufgabe_1/siu.mp3")

