import turtle

from Aufgabe_3.alphabet import *
from Aufgabe_3.move import *
from Aufgabe_3.punctuation import *
from Aufgabe_3.alphabet2 import *

tur = turtle.Turtle()

character = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z,
    ".": point,
    #"?": None,
    #"!": None,
}

# character = {
#     "a": printA,
#     "b": printB,
#     "c": printC,
#     "d": printD,
#     "e": printE,
#     "f": printF,
#     "g": printG,
#     "i": printI,
#     "j": printJ,
#     "k": printK,
#     "l": printL,
#     "m": printM,
#     "n": printN,
#     "o": printO,
#     "p": printP,
#     "q": printQ,
#     "r": printR,
#     "s": printS,
#     "t": printT,
#     "u": printU,
#     "v": printV,
#     "w": printW,
#     "x": printX,
#     "y": printY,
#     "z": printZ,
#     ".": point,
#     #"?": None,
#     #"!": None,
# }

moveTurtle = {
    "W": forward,
    "S": backwards,
    "A": rotateLeft,
    "D": rotateRight,
    "G": moveDown,
    "F": moveUp
}

def options_to_print():
    print("Enter 1 to write a letter ")
    print("Enter 2 to add a character to program ")
def print_turtle_commands():
    moveTurtle.values()

def writeTurtle():
    while True:
        options_to_print()
        option = input("Enter your option for the program: ".strip())

        if option == "1":
            optionCharacter = input("Write a letter ").strip()
            if optionCharacter in character:
                character[optionCharacter](tur)
            else:
                continue

        elif option == "2":
            print_turtle_commands()
            while True:
                yOption = input("Your character ").strip()
                if option in moveTurtle:
                    moveTurtle[yOption]()
                else:
                    break

        else:
            tur.clear()
            break
#writeTurtle()



