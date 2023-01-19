from functools import reduce
from itertools import chain

def ub1(even_row = False):
    with open("zahlen.txt") as f:
        content = f.readlines()


    lines = list(map(lambda line: line.strip("\n").split("UBB"), content))



    numbers = list(map(lambda line: list(map(lambda string: int(string), line)), lines))

    #return lines

    if even_row:
        even_lines = list(map(lambda desired_lines: list(filter(lambda number: number % 2 == 0, desired_lines)), numbers))

        res = sum(list(chain(*even_lines)))
        print(res)

    else:
        odd_lines = list(map(lambda desired_lines: list(filter(lambda number: number % 2 == 1, desired_lines)), numbers))

        res = sum(list(chain(*odd_lines)))
        print(res)

    return res




def correct_test():
    assert ub1(True) == 14 + 4 + 22 + 18 + 20 + 26 + 12 + 22 + 4 + 0 + 12 + 0 + 8 + 12 + 2 + 2 + 4


def incorrect_test():
    try:
        assert ub1() == 2

    except AssertionError:
        print("Incorrect")



def test():
    correct_test()
    incorrect_test()
test()

def main():
    print(ub1(True))
    print(ub1(False))

main()