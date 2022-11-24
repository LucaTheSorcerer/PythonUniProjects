def extractFile(fileName):
    """
    This function is used to extract the contents of a file in variable
    :param fileName: The name of the file to be accessed
    :return: A list that contains the contents of the file
    """
    l = []

    with(open(fileName) as file):
        for line in file:
            l.append(line.strip())

    return l


def changeWords(word, filename, replaceWord, lst):
    """
    This function changes all occurrences of a word in the list
    :param lst: The list where the words of the original file are stored
    :param word: the word to be replaced
    :param filename: the name of the file
    :param replaceWord: The word you replace the former word with
    """
    wordAp = 0
    newLst = []
    for s in lst:
        s = s.split(" ")
        for w in s:
            if w == word:
                wordAp += 1
                s[s.index(w)] = replaceWord
        newLst.append(s)
    print(f"The word appears {wordAp} times")
    print(newLst)

    changeWordsInFile(filename, newLst)


def changeWords2(wordToReplace, filename, replaceWord, lst):
    wordAp = 0

    for i in range(len(lst)):
        # print(line)
        while lst[i].find(wordToReplace) != -1:
            lst[i] = lst[i].replace(wordToReplace, replaceWord)
            wordAp += 1

    print(f"The word appears {wordAp} times")
    # print(lst)

    changeWordsInFile(filename, lst)


def changeWordsInFile(fileName, wordLst):
    """
    :param fileName: The name of the file
    :param wordLst: A list of all the word to be placed in the file
    The specified file will be changed according to the changes in the list
    """
    f = open(fileName, "w")

    for line in wordLst:
        for wd in line:
            f.write(wd)
        f.write("\n")


def call_changeWords():
    """
    This function is used to tie everything together
    """
    fl = input("FileName ").strip()

    try:
        fileText = extractFile(fl)
    except FileNotFoundError as ex:
        print(ex)
        return

    word = input("Enter word to be replaced ").strip()
    replacementWord = input("Enter the replacement word ").strip()

    changeWords2(word, fl, replacementWord, fileText)
call_changeWords()