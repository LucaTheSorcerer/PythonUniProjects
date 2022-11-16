matrix = [
    [2, 5, 3, 2],
    [2, 2, 4, 4],
    [3, 2, 2, 2],
    [5, 3, 5, 2]
]


def add_with_minimal_element(matrix):
    minim = float('inf')
    maxim = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < minim:
                minim = matrix[i][j]
            if matrix[i][j] > maxim:
                maxim = matrix[i][j]

    for i in range(len(matrix)):
        if matrix[i][j] != maxim:
            pass
        else:
            for j in range(len(matrix)):
                matrix[i][j] += minim
    return matrix

print(add_with_minimal_element(matrix))