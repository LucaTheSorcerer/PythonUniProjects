from functools import reduce


def read_from_file():
    with open("zahlen.txt", "r") as f:
        lines = list(map(lambda line: line.strip("\n").split("\t"), f.readlines()))
        # reads from the file and creates a list of lists containing strings
        numbers = list(map(lambda line: list(map(lambda string: int(string), line)), lines))
        # converts the elements of the list of lists from string to int
        return numbers


print(read_from_file())


def ub1(greatest=True):
    content = read_from_file()

    if greatest:
        # generating the biggest number form the lists
        max_list = list(map(lambda numbers_list: reduce(lambda a, b: max(a, b), numbers_list), content))
        product = reduce(lambda a, b: a * b, max_list)
    else:
        # generating the smallest number form the lists
        min_list = list(map(lambda numbers_list: reduce(lambda a, b: min(a, b), numbers_list), content))
        product = reduce(lambda a, b: a * b, min_list)

    return product


print(ub1())

# Successful test
assert ub1() == 25 * 29 * 27 * 26 * 15 * 23

# Unsuccessful test
try:
    assert ub1() == "s"
except AssertionError:
    print("Muie Mic")

