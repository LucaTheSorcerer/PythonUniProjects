from Aufgabe_3.data.data import moveTrt

def options_to_print():
    print("Enter 1 to write a word ")
    print("Enter 2 in order draw and add a new character ")


def printTurtleCommands():
    moveTrt.values()

def printUserOptions():
    print("Your options are: \n"
          "Press W to move forward 10 pixels \n"
          "Press S to move backwards 10 pixles \n"
          "Press A to rotate left \n"
          "Press D to rotate right \n"
          "Press G to put pen down \n"
          "Press F to put pen up")