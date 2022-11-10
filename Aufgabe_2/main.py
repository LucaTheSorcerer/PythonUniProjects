def FileExractor(filename):
    """
    It extracts all the lines in f and append them to a new list
    :param filename:
    :return:
    """
    l = []
    with open(filename) as f:
        for line in f:
            l.append(line.strip())

    return l


def WordsChange(word, filename, replacementWord, listt):
    """
    It changes all the occurences of a word with the desired given word and keeps a counter of the appearences
    :param word:
    :param filename:
    :param replacementWord:
    :param listt:
    :return:
    """
    counter = 0
    new_list = []
    for s in listt:
        s = s.split(" ")
        for w in s:
            if w == word:
                counter += 1
                s[s.index(w)] = replacementWord
        new_list.append(s)
    print(f"The replacement word appears {counter} times")
    print(new_list)

    changeWordsInFile(filename, new_list)


def changeWordsInFile(fileName, wordList):
    """
    It replaces the list of words after being replaced in the same file
    :param fileName: file's name
    :param wordList: list of all words to be placed in the file again
    :return:
    """
    f = open(fileName, "w")

    for line in wordList:
        for word in line:
            f.write(word + " ")
        f.write("\n")


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
# changeWords_to_call_WordsChange()
