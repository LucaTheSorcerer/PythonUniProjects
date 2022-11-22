from Aufgabe_2.change_words.words_change import *
from Aufgabe_2.file_extractor.file_extractor import *
def changeWords_to_call_WordsChange():
    f1 = "Aufgabe_2/aufgabe2.txt"
    """
    This calls the WordsChange function and it takes input as input the replaceable word and the word to replace 
    it with
    """
    fileText = []

    try:
        fileText = FileExractor(f1)  # If file does not exist then it outputs that file does not exist
    except FileNotFoundError:
        print("File not found!")
        return

    word = input("Enter name of the word to be replaced ").strip()
    word_replacement = input("Enter the word used for replacement: ").strip()

    WordsChange(word, f1, word_replacement, fileText)