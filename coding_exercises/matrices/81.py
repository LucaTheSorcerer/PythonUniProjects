matrix = [
    [1, 5, 1, 1],
    [2, 1, 2, 3],
    [1, 3, 4, 2],
    [2, 1, 2, 1]
]


def bigger_than_neighbours(matrix):
    list_of_bigger_numbers = []
    counter = 0

    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         if i == 0 or i == len(matrix) + 1 or j == 0 or j == len(matrix) + 1:
    #                 matrix[i][j] = -1

    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1):
            if matrix[i][j] > matrix[i+1][j] and matrix[i][j] > matrix[i][j+1] and matrix[i][j] > matrix[i-1][j] and matrix[i][j] > matrix[i][j-1]:
                counter += 1
            else:
                pass
    return counter
print(bigger_than_neighbours(matrix))