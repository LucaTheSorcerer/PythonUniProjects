matrix = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

def spiral_matrix(matrix):
    """
    ToDo:
        -print first row from the remaining rows
        -print last columnn from the remaining columns
        -print last row from the remaining rows
        -print first columns from the remaning columns
    :param matrix:
    :return:
    """
    starting_row_index = 0
    ending_row_index = len(matrix)
    starting_column_index = 0
    ending_column_index = len(matrix[0])

    while (starting_row_index < ending_row_index and starting_column_index < ending_column_index):

        #Print first row from the remaining rows
        for i in range(starting_column_index, ending_column_index):
            print(matrix[starting_row_index][i])
        starting_row_index += 1

        #Printing last column from the remaning columns
        for i in range(starting_row_index, ending_row_index):
            print(matrix[i][ending_column_index-1])
        ending_column_index -= 1

        #Print bottom row from the remaining rows
        if starting_row_index < ending_row_index:
            for i in range(ending_column_index-1, starting_column_index-1, -1):
                print(matrix[ending_row_index-1][i])
        ending_row_index -= 1


        #Print first column from the remaining columns
        if starting_column_index < ending_column_index:
            for i in range(ending_row_index-1, starting_row_index-1, -1):
                print(matrix[i][starting_column_index])
        starting_column_index += 1



    return
spiral_matrix(matrix)

