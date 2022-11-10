import random

wordList = ["dog", "cat", "snake", "elephant", "tiger", "lion", "giraffe", "wolf", "dolphin"]
alphabet = "abcdefghiklmnopqrtsuvwxyz"

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']


def get_random_word_for_hangman(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    word = wordList[wordIndex]
    return word
#print(get_random_word(wordList))

def story():
    print("Welcome to the hangman game!")
    print("It is a cold morning! The people have gathered around in big crowds to watch how a man will be executed")
    print("He will be executed by hanging!")
    print("His only chance to escape the tight rope is to guess a word that only the executioner knows")
    print("Welcome to the hangman! Try not to get executed: ")
    print()
    print("Hint: The executioner loves animals")
print(story())

def display_game_board(missedLetter, correctLetter, secretWord):
    print(HANGMAN_PICS[len(missedLetter)])
    print()
    print('Missed letters: ', end = ' ')
    for letter in missedLetter:
        print(letter, end = ' ')
    print()
    print('Correct letters: ', end = ' ')

    blanks = '_' * len(secretWord)

    """
    This for loops replaces each letter in the secret word with a blank space correctly
    """
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetter:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]


    for letter in blanks:
        print(letter, end = ' ')
    print()


def get_player_guess(alreadyGuessed):

    """
    This function returns the letter the player has guessed. This function makes sure that the player entered a single
    letter and not more than that
    :param alreadyGuessed:the word the player has chosen
    :return:it returns the letter the player has guessed
    """
    while True:
        print("Take a guess at a letter to save yourself")
        guess = input().lower()
        if 1 != len(guess):
            print("Invalid option! Pick only one letter")
        elif guess in alreadyGuessed:
            print("You already guessed this letter! Choose again")
        elif guess not in alphabet:
            print("Choose a letter and not something else!")
        else:
            return guess

def playAgain():
    """
    This function asks the users if he wants to play again and returns True if the input is equal to True,
    stops the game otherwise
    :return:
    """
    print("Do you want to play again?")
    return input().lower().startswith("y")

print("H A N G M A N")
missedLetters = ' '
correctLetters = ' '
secretWord = get_random_word_for_hangman(wordList)
gameIsFinished = False

while True:
    display_game_board(missedLetters, correctLetters, secretWord)

    guess = get_player_guess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetter = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetter = False
                break
        if foundAllLetter:
            print(f"The secret word is {secretWord}")
            print("You are not dying today! Congrats! You beat the executioner at it's own game")
            gameIsFinished = True


    else:
        missedLetters = missedLetters + guess
        if(len(missedLetters)) == len(HANGMAN_PICS) - 1:
            display_game_board(missedLetters, correctLetters, secretWord)
            print("You have lost! You died! Press F in the chat to pay respects!")
            print(f"You ran out of gusses! The missed letters are {missedLetters} and the correct letters are"
                  f"{correctLetters} ")
            print(f"The secret word was {secretWord}")
            gameIsFinished = True

    if gameIsFinished:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsFinished = False
            secretWord = get_random_word_for_hangman(wordList)
        else:
            break

