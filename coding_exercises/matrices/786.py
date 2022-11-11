import numpy as np

matrix = [
    [3, 1, 8, 5],
    [7, 8, 5, 1],
    [2, 2, 6, 7],
    [9, 8, 1, 3]
]

def symmetrical_first_diagonal(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix.append(matrix[j][i])

    array = np.reshape(new_matrix, (4,4))
    return array
print(symmetrical_first_diagonal(matrix))