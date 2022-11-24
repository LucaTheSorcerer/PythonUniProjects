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
            f.write(word)
        f.write("\n")