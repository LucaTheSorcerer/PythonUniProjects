import random

def get_random_word_for_hangman(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    word = wordList[wordIndex]
    return word