matrix = [
    [3, 1, 8, 5, 4],
    [7, 8, 5, 1, 2],
    [2, 2, 6, 7 ,3],
    [9, 8 ,1 ,3 ,6],
    [7, 5, 3, 1, 7]
]

def sum_of_four_zones(matrix):
    """
    This function calculates the sum of the four zone marked by the two diagonals (N, S, W, E)
    :param matrix: matrix as input
    :return: returns the sum of every zone in a list
    """
    sum_nord = 0
    sum_south = 0
    sum_east = 0
    sum_west = 0
    list_of_sums = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            #For nord
            if i < j and i + j < len(matrix) -1:
                sum_nord += matrix[i][j]

            #For south
            elif i > j and i + j > len(matrix)-1:
                sum_south += matrix[i][j]

            elif i > j and i + j < len(matrix)-1:
                sum_west += matrix[i][j]

            elif i < j and i + j > len(matrix)-1:
                sum_east += matrix[i][j]
    list_of_sums.append(sum_nord)
    list_of_sums.append(sum_south)
    list_of_sums.append(sum_west)
    list_of_sums.append(sum_east)

    list_of_sums.sort()
    return list_of_sums
print(sum_of_four_zones(matrix))

def test():
    assert sum_of_four_zones(matrix) == [10, 18, 19, 20]
    assert not sum_of_four_zones(matrix) == [19, 10, 20, 19]
test()