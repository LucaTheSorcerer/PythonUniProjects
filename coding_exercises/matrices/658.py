matrix = [
    [4, 20, 15, 23],
    [1, 8, 23, 22],
    [17, 15, 13, 18],
    [3, 18, 8, 20],
]

def sum_on_every_line(matrix):
    """
    This function returns the sum of every line of the quadratic matrix
    :param matrix: takes as input a matrix
    :return: return the sum
    """
    list_of_sums = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[i][j]
        list_of_sums.append(sum)
    return list_of_sums
print(sum_on_every_line(matrix))
