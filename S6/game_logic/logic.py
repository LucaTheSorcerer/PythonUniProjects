from S6.ui import console

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

"""
#with open("zahlen.txt") as f:
 #       content = f.readlines()
        lines = list(map(lambda line: line.strip("\n").split("\t"), content))

        numbers = list(map(lambda line: list(map(lambda string: int(string), line)), lines))
"""