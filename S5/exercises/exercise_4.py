def longest_word_in_file(f):
    list = []
    for line in f:
        line = line.split('\n')[0]
        print(line)
        words = line.split(' ')
        longest_word = 0
        for word in words:
            if len(word) > longest_word:
                longest_word = len(word)
        list.append(longest_word)
    return list



def read_from_file():
    with open("exercise_4.txt") as f:
        result = longest_word_in_file(f)
        print(result)
read_from_file()