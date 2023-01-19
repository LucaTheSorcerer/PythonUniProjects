a = "1212312231231"
b = "5553412313231"

def big_sum(string1, string2):
    """
    This function takes as input two strings made of numbers and returns the sum of
    the two strings in another string
    :param string1: paramter for the first string
    :param string2: parameter for the second string
    :return: return the result after the sum
    """
    result = ' '
    for i in range(len(string1)-1, -1, -1):
        cif = int(string1[i]) + int(string2[i])
        carry = cif // 10
        result = str(cif % 10 + carry) + result
    if carry > 0:
        result = str(carry) + result
    return result
print(big_sum(a, b))






















"""
def read_from_file():
    with open("zahlen.txt", "r") as f:
        lines = list(map(lambda line: line.strip("\n").split("\t"), f.readlines()))
        # reads from the file and creates a list of lists containing strings
        numbers = list(map(lambda line: list(map(lambda string: int(string), line)), lines))
        # converts the elements of the list of lists from string to int
        return numbers


print(read_from_file())


returns the product of the biggest numbers in list if greatest = True and min otherweise
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
"""

