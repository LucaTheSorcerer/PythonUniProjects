matrix = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3],
    [6, 3, 4],
    [7, 8, 9]
]

def matrix_is_sorted(list):
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True

def add_all_elements_from_matrix_to_list(matrix):
    new_list = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix)):
                new_list.append(matrix[i][j])
        else:
            for j in range(len(matrix)-1, -1, -1):
                new_list.append(matrix[i][j])

    if matrix_is_sorted(new_list):
        return True
    else:
        return False
print(add_all_elements_from_matrix_to_list(matrix))

def test():
    assert add_all_elements_from_matrix_to_list(matrix) == True
    #assert add_all_elements_from_matrix_to_list(matrix2) == True
test()