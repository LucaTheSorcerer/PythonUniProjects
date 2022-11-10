def isPalindrome(list):
    return list == list[::-1]

def determine_palindrome_from_file(list):
    dict = {}
    for line in list:
        line = line.split("\n")[0]
        print(line)
        words = line.split(" ")
        for word in words:
            if isPalindrome(word):
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1

    return dict


def read_from_file():
    with open("exercise_5.txt") as f:
        result = determine_palindrome_from_file(f)
        print(result)
read_from_file()