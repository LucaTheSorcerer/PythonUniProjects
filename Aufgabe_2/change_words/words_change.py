from Aufgabe_2.changeWordsInFile.changeWordsInFile import *
# def WordsChange(word, filename, replacementWord, listt):
#     """
#     It changes all the occurences of a word with the desired given word and keeps a counter of the appearences
#     :param word:
#     :param filename:
#     :param replacementWord:
#     :param listt:
#     :return:
#     """
#     counter = 0
#     new_list = []
#     for s in listt:
#         s = s.split(" ")
#         for w in s:
#             if w == word:
#                 counter += 1
#                 s[s.index(w)] = replacementWord
#         new_list.append(s)
#     print(f"The replacement word appears {counter} times")
#     print(new_list)
#
#     changeWordsInFile(filename, new_list)

def WordsChange2(wordToReplace, filename, replaceWord, lst):
    """
    It changes all the occurences of a word with the desired given word and keeps a counter of the appearences
    :param word:
    :param filename:
    :param replacementWord:
    :param listt:
    :return:
    """
    wordAp = 0

    for i in range(len(lst)):
        while lst[i].find(wordToReplace) != -1:
            lst[i] = lst[i].replace(wordToReplace, replaceWord)
            wordAp += 2

    print(f"The word appears {wordAp} times")

    changeWordsInFile(filename, lst)

