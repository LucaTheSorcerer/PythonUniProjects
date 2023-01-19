from functools import reduce
from statistics import mean


def ub1(subject):
    with open("text.txt") as f:
        content = f.readlines()

    lines = list(map(lambda line: line.strip("\n").split(","), content))

    desired_lines = list(filter(lambda line: line[-2] == subject, lines))

    desired_grades = list(map(lambda grade : int(grade[-1]), desired_lines))

    average_grades = reduce(lambda number1, number2: number1 + number2, desired_grades) / len(desired_grades)


    return  average_grades

def correct_test():
    assert ub1("Advanced programming") == 8.166666666666666

def incorrect_test():
    try:
        assert ub1("Advanced programming") == 2
    except AssertionError:
        print("wtf")


def test():
    correct_test()
    incorrect_test()
test()


def main():
    print(ub1("Advanced programming"))
main()