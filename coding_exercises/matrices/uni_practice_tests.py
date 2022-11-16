matrix = [
    [12, 6, 3, 0],
    [13, 7, 4, 1],
    [14, 8, 5, 2],
    [15, 10, 11, 9]
]



def outer_square(matrix):
    new_list = []


    #First line:
    for i in range(len(matrix)):
        new_list.append(matrix[0][i])

    #Last column
    for i in range(1, len(matrix)):
        new_list.append(matrix[i][len(matrix)-1])

    #Last row revered
    for i in range(len(matrix)-2, -1, -1):
        new_list.append(matrix[len(matrix)-1][i])

    #First column reversed
    for i in range(len(matrix)-2, 0, -1):
        new_list.append(matrix[i][0])

    #Center square

    return new_list
print(outer_square(matrix))
