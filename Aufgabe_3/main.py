import turtle
from Aufgabe_3.letters.alphabet import *
from Aufgabe_3.move import *
from Aufgabe_3.punctuation import *

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
    print("Enter 2 in order to move your turtle ")
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
            print("Your options are: \n"
                  "Press W to move forward 10 pixels \n"
                  "Press S to move backwards 10 pixles \n"
                  "Press A to rotate left \n"
                  "Press D to rotate right \n"
                  "Press G to put pen down \n"
                  "Press F to put pen up")
            #print_turtle_commands()

            f = open("Aufgabe_3/user_input.txt", "w")  # Save the user input into the text file

            while True:
                yOption = input("Your character ").strip()
                if yOption in moveTurtle:
                    moveTurtle[yOption](tur)
                    f.write(str(moveTurtle[yOption](tur)))
                else:
                    break


        else:
            tur.clear()
            break
#writeTurtle()



