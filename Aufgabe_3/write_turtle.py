import turtle
from Aufgabe_3.program_logic.logic import *
from Aufgabe_3.ui.ui import *

tur = turtle.Turtle()

def writeToTurtle():
    fileWords = fillFileWordsList()
    while True:
        interpretListfromFile()

        options_to_print()
        option = input("Enter your desired option: ").strip()

        fileWords = fillFileWordsList()

        if option == "1":
            optionChr = input("Enter a word ").strip()
            writeCharacterList(tur, optionChr)

        elif option == "2":
            printUserOptions()
            characterCreation(tur, fileWords)

        else:
            saveAdditionalChr(fileWords)
            tur.clear()
            break