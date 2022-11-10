def isPalindrome(list):
    return list == list[::-1]

def check_every_line_ifpalindromeexists(lines):
    dict = {}
    for line in lines:
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

def read_from_file_and_write_over():
    with open("exercise_6.txt") as f:
        data = check_every_line_ifpalindromeexists(f)

    f = open("exercise_6_writeover.txt", "w")

    for element in data:
        f.write((element + " ") * data[element])
read_from_file_and_write_over()