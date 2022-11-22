from Aufgabe_3.data.data import *
from Aufgabe_3.ui.ui import *


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


def saveAdditionalChr():
    """
    Saves the contents of AdditionalChr to the file
    :return:
    """
    f = open("Aufgabe_3/user_input.txt", "w")

    for key in additionalChr:
        f.write(":" + key + ":" + "+" + "\n")
        s = additionalChr[key]
        s = s.strip()
        s = s.split("+")

        for word in s:
            if word != "":
                f.write(word + "+" + "\n")

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

    auxName = characterName.split(":")[1]
    additionalChr[auxName] = ""
    printUserOptions()

    fileWords.append(characterName)

    while True:
        yOption = input("Your character ").strip()
        if yOption in moveTrt:
            moveTrt[yOption](tur)
            fileWords.append(str(moveTurtleName[yOption]))
            additionalChr[auxName] += str(moveTurtleName[yOption] + "+")
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
        tur.pd()
        interpretListOfCharacters(additionalChr[optionChr], tur)
        tur.fd(30)
        tur.pu()


def writeCharacterList(tur, st):
    """
    This function splits the given word into separate characters in order for the turtle to write
    the characters
    :param tur: the turtle
    :param st: word entered by the user
    :return: --
    """
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
    Interprets the command and executes it
    :param s: a string containing the command
    :param tur: turtle used to draw character
    :return:
    """
    if s in moveTrtInterpretation:
        moveTrtInterpretation[s](tur)


def interpretListOfCharacters(l, tur):
    """
    This function executes all the commands from the list
    :param l: list of commands as a single string of commands
    :param tur: the turtle
    :return:
    """
    l = l.split("+")
    for s in l:
        interpretCharacter(s, tur)


def interpretListfromFile():
    """
    This function interprets the contents of the given file and saves them in the additionalChr dictionary
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
