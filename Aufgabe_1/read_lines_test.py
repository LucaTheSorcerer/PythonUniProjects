
def read_lines_for_rock():
    specified_lines = [0, 1, 2, 3, 4, 5, 6, 7]

    with open("Aufgabe_1/ascii_characters.txt") as f:
        for pos, l_num in enumerate(f):
            if pos in specified_lines:
                print(l_num)
read_lines_for_rock()

def read_lines_for_paper():
    specified_lines = [8, 9, 10, 11, 12, 13, 14, 15]
    with open("Aufgabe_1/ascii_characters.txt") as f:
        for pos, l_num in enumerate(f):
            if pos in specified_lines:
                print(l_num)
read_lines_for_paper()

def read_lines_for_scissors():
    specified_lines = [16, 17, 18, 19, 20, 21, 22, 23]
    with open("Aufgabe_1/ascii_characters.txt") as f:
        for pos, l_num in enumerate(f):
            if pos in specified_lines:
                print(l_num)
read_lines_for_scissors()


