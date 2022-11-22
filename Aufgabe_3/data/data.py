from Aufgabe_3.letters.alphabet import *
from Aufgabe_3.punctuation_signs.punctuation import *
from Aufgabe_3.move_turtle.move import *

"""
This dictionary stores all the functions for the characters
"""
characterDict = {
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
    "?": question_mark,
    "!": exclamation_mark
}

"""
This  dictionary stores the new characters that are created by the user
"""
additionalChr = {}

moveTrt = {
    "W": moveForward,
    "S": moveBackwards,
    "A": rotateLeft,
    "D": rotateRight,
    "G": moveDown,
    "F": moveUp
}


"""
This is the string version of the dictionary moveTrt
"""
moveTurtleName = {
    "W": "forward",
    "S": "backwards",
    "A": "rotateLeft",
    "D": "rotateRight",
    "G": "moveDown",
    "F": "moveUp"
}

"""
This dictionary creates a link between what it needs to be executed and what is being
read from the file
"""
moveTrtInterpretation = {
    "forward":moveForward,
    "backwards":moveBackwards,
    "rotateLeft":rotateLeft,
    "rotateRight":rotateRight,
    "moveDown":moveDown,
    "moveUp":moveUp
}