import turtle
from Aufgabe_3.program_logic.logic import *
from Aufgabe_3.ui.ui import *
from playsound import playsound

tur = turtle.Turtle()

def writeToTurtle():
    interpretListfromFile()
    fileWords = fillFileWordsList()

    while True:

        options_to_print()
        option = input("Enter your desired option: ").strip()

        if option == "1":
            optionChr = input("Enter a word ").strip()
            writeCharacterList(tur, optionChr)
            playsound("Aufgabe_3/omg.mp3")

        elif option == "2":
            characterCreation(tur, fileWords)

        else:
            saveAdditionalChr()
            tur.clear()
            break