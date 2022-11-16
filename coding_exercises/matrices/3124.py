matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

matrix2 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 12, 6]
]




def magic_square(matrix):
    """
    This function checks if a quadratic matrix is a perfect square
    The sum on every line, column and diagonal have to be equal in order for the matrix
    to be a perfect square
    :param matrix:
    :return: returns True if the sums are equal, false otherweise
    """
    total_sums = []
    for i in range(len(matrix)):
        sum_of_line = 0
        for j in range(len(matrix)):
            sum_of_line += matrix[i][j]
        total_sums.append(sum_of_line)

    for i in range(len(matrix)):
        sum_of_column = 0
        for j in range(len(matrix)):
            sum_of_column += matrix[j][i]
        total_sums.append(sum_of_column)

    sum_first_diagonal = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                sum_first_diagonal += matrix[i][j]
    total_sums.append(sum_first_diagonal)

    sum_second_diagonal = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i + j == (len(matrix)) - 1:
                sum_second_diagonal += matrix[i][j]
    total_sums.append(sum_second_diagonal)

    first_element = total_sums[0]
    result = True
    for number in total_sums:
        if first_element != number:
            result = False
    return result
print(magic_square(matrix))

def test():
    assert magic_square(matrix) == True
    assert not magic_square(matrix2) == True
test()