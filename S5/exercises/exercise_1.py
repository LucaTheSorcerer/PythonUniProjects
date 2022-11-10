matrix = [
    [4, 3, 10],
    [1, 2, 10],
    [1, 1, 8]
]

def call_sum_on_each_column_matrix():
    return sum_on_each_column_matrix()



def sum_on_each_column_matrix(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]

        if not is_perfect_number(sum):
            print(False)
            return False
    print(True)
    return True



def is_perfect_number(number):
    """
    This function takes as input a number that represents the sum on each columns and checks if the number is equal
    to the sum of its divisors
    :param number: sum of the column
    :return: return True if the number is equal to the sum of its divisors
    """
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum += i
    return number == sum

sum_on_each_column_matrix(matrix)

def test():
    assert is_perfect_number(6)
    assert not is_perfect_number(29)
    assert is_perfect_number(28)
    return
test()







