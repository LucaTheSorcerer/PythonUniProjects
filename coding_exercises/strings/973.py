sentence = "ei pazesc o oaie"

def append_words_to_list(sentence):
    list_of_words = []
    list_of_words = list_of_words + sentence.split(" ")
    return  list_of_words

append_words_to_list(sentence)


def counter_vocals(list):
    vocals = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    list_of_words = []
    list_of_words = list_of_words + list.split(" ")
    for word in list_of_words:
        if consonants in word:
            list_of_words.remove(word)
    return list_of_words
print(counter_vocals(sentence))


