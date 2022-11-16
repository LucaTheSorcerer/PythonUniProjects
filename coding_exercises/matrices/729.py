matrix = [
    [10, 8, 5, 8, 4, 2],
    [6, 5, 3, 1, 3, 6],
    [8, 1, 4, 7, 8, 8],
    [5, 1, 9, 6, 6, 1],
    [8, 9, 10, 1, 3, 6],
    [8, 2, 3, 3, 9, 6]
]

def numbers_west_zone(matrix):
    west_elements_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j and i + j < len(matrix) - 1:
                west_elements_list.append(matrix[i][j])

    west_elements_list = set(west_elements_list)
    west_elements_list = list(west_elements_list)
    west_elements_list.sort()
    return west_elements_list


print(numbers_west_zone(matrix))