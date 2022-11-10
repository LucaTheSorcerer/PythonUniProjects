word = "Terminator"

def change_vocals(string1):
    """
    This function takes as paramter a string and reverses only the order of the vocals
    :param string1: This is the word on which we will reverse the vocals order
    :return: it returns a new string with the vocals order reversed
    """
    vocals = "aeiou"
    list_with_vocals = []
    for word in range(len(string1)-1):
        if string1[word] in vocals:
            list_with_vocals.append(string1[word])
    print(list_with_vocals)

    new_string = " "
    i = -1
    for char in string1:
        if char not in list_with_vocals:
            new_string += char
        else:
            new_string += list_with_vocals[i]
            i -= 1
    return new_string

print(change_vocals(word))