matrix = [
    [4, 20, 15, 23],
    [1, 8, 23, 22],
    [17, 15, 13, 18],
    [3, 18, 8, 20],
]


def sum_of_both_diagonals(matrix):
    """
    This function returns the sum of the both diagonals of the matrix
    :param matrix: the inputs is a matrix or a nested list
    :return: sum of both diagonals
    """
    sum_first_diagonal = 0
    sum_second_diagonal = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                 sum_first_diagonal += matrix[i][j]
            if ((i + j) == (len(matrix)-1)):
                sum_second_diagonal += matrix[i][j]
    return abs(sum_first_diagonal + sum_second_diagonal)
print(sum_of_both_diagonals(matrix))

def test():
    """
    This test the function sum_of_both_diagonals
    :return:
    """
    assert sum_of_both_diagonals(matrix) == 109
    assert not sum_of_both_diagonals(matrix) == 108
test()
