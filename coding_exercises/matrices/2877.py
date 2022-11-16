import numpy as np
matrix = [
    [4, 1, 3],
    [9, 6, 8],
    [5, 2, 7]
]

def order_lines_columns(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            if matrix[i][j] > matrix[i][j+1]:
                aux = matrix[i][j]
                matrix[i][j] = matrix[i][j+1]
                matrix[i][j+1] = aux
            else:
                pass

    for i in range(len(matrix)-1):
        for j in range(len(matrix)):
            if matrix[j][i] > matrix[j][i+1]:
                aux = matrix[j][i]
                matrix[j][i] = matrix[j][i+1]
                matrix[j][i+1] = aux

    array = np.reshape(matrix, (3,3))
    return array
print(order_lines_columns(matrix))