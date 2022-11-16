from Aufgabe_3.data.data import *


def fillFileWordsList():
    """
    This function is used to open a file and return all the characters defined by
    the user
    :return: The list filled with used defined characters
    """
    fileWords = []
    with open("Aufgabe_3/user_input.txt") as f:
        for line in f:
            fileWords.append(line.strip())

    return fileWords


def saveAdditionalChr(fileWords):
    f = open("Aufgabe_3/user_input.txt")

    for word in fileWords:
        if "+" not in fileWords:
            f.write(word + "+" + "\n")
        else:
            f.write(word + "\n")
    f.close()

def characterCreation(tur, fileWords):
    """
    This function creates a new character and stores it into the user_input.txt
    file
    :param tur: this is paramter for the Turtle
    :param characterName: The name of the user defined character
    :param fileWords: The list that contains all the user defined charactes in the file
    :return: --
    """

    characterName = ":" + input("Name your character ") + ":"

    if characterName in fileWords:
        print("Invalid name! Character already exists")
        return

    fileWords.append(characterName)

    while True:
        yOption = input("Your character ").strip()
        if yOption in moveTrt:
            moveTrt[yOption](tur)
            fileWords.append(str(moveTurtleName[yOption]))
        else:
            break



def writeCharacter(tur, optionChr):
    """
    This function is used to write a letter from the dictionary of options,
    including user defined characters
    :param tur:
    :return:
    """
    if optionChr in characterDict:
        tur.pd()
        characterDict[optionChr](tur)
        tur.pu()

    if optionChr in additionalChr:
        tur.od()
        interpretListOfCharacters(additionalChr[optionChr], tur)
        tur.fd(30)
        tur.pu()


def writeCharacterList(tur, st):
    newS = []
    s = ""

    for c in st:
        if s in additionalChr:
            newS.append(s)
            s = ""
        if c in characterDict:
            newS.append(c)
        else:
            s += c

    if s in additionalChr:
        newS.append(s)

    for e in newS:
        writeCharacter(tur, e)


def interpretCharacter(s, tur):
    """
    This function transfroms the string characters into code by using a dictionary
    and executes the command
    :param s: a string containing the command
    :param tur: turtle used to draw character
    :return:
    """
    if s in moveTrtInterpretation:
        moveTrtInterpretation[s](tur)


def interpretListOfCharacters(l, tur):
    """
    This function executed all the commands from the list
    :param l: list of commands as a single string of commands
    :param tur: the turtle
    :return:
    """
    l = l.split("+")
    for s in l:
        interpretCharacter(s, tur)


def interpretListfromFile():
    """
    This function takes the commands as stringsfrom the user_input file and
    stores them in the dictionary that contains user defined characters
    :return: --
    """
    s = ""
    with open("Aufgabe_3/user_input.txt") as f:
        for line in f:
            line = line.strip()
            s += line
    s = s.split(":")

    for i in range(1, len(s) - 1, 2):
        additionalChr[s[i]] = s[i + 1]
