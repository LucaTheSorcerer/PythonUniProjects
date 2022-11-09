def FileExractor(filename):
    l = []
    with open(filename) as f:
        for line in f:
            l.append(line.strip())

    return l


def WordsChange(word, filename, replacementWord, listt):
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
    f = open(fileName, "w")

    for line in wordList:
        for word in line:
            f.write(word + " ")
        f.write("\n")

def changeWords_to_call_WordsChange():
    f1 = "aufgabe2.txt"
    """
    """
    fileText = []

    try:
        fileText = FileExractor(f1)
    except FileNotFoundError:
        print("File not found!")
        return

    word = input("Enter name of the word to be replaced ").strip()
    word_replacement = input("Enter the word used for replacement: ").strip()

    WordsChange(word, f1, word_replacement, fileText)