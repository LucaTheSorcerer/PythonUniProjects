from Aufgabe_3.letters.alphabet import *
from Aufgabe_3.punctuation_signs.punctuation import *
from Aufgabe_3.move_turtle.move import *

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

additionalChr = {}

moveTrt = {
    "W": moveForward,
    "S": moveBackwards,
    "A": rotateLeft,
    "D": rotateRight,
    "G": moveDown,
    "F": moveUp
}


moveTurtleName = {
    "W": "forward",
    "S": "backwards",
    "A": "rotateLeft",
    "D": "rotateRight",
    "G": "moveDown",
    "F": "moveUp"
}

moveTrtInterpretation = {
    "forward":moveForward,
    "backwards":moveBackwards,
    "rotateLeft":rotateLeft,
    "rotateRight":rotateRight,
    "moveDown":moveDown,
    "moveUp":moveUp
}