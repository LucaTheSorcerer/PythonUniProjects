matrix = [
    [4, 20, 15, 23],
    [1, 8, 23, 22],
    [17, 15, 13, 18],
    [3, 18, 8, 20],
]


def even_elements_sum(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            if matrix[i][j] % 2 == 0:
                sum += matrix[i][j]
            else:
                pass

    return sum
print(even_elements_sum(matrix))




