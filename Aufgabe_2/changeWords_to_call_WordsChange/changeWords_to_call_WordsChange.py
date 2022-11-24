from Aufgabe_2.change_words.words_change import *
from Aufgabe_2.file_extractor.file_extractor import *


def changeWords_to_call_WordsChange():
    """
    This calls the WordsChange function, and it takes input as input the replaceable word and the word to replace
    it with
    """
    f1 = input("FileName ").strip()

    try:
        fileText = FileExractor(f1)  # If file does not exist then it outputs that file does not exist
    except FileNotFoundError as error:
        print(error)
        return

    word = input("Enter name of the word to be replaced ").strip()
    word_replacement = input("Enter the word used for replacement: ").strip()

    WordsChange2(word, f1, word_replacement, fileText)
