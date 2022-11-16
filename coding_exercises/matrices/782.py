matrix = [
    [10, 8, 5, 8, 4, 2],
    [6, 5, 3, 1, 3, 8],
    [8, 1, 4, 7, 8, 8],
    [5, 1, 9, 6, 6, 1],
    [8, 9, 3, 2, 3, 6],
    [8, 9, 3, 3, 9, 6]
]

matrix2 = [
    [10, 8, 5, 8, 4, 2],
    [6, 5, 3, 1, 3, 8],
    [8, 1, 4, 7, 8, 8],
    [5, 1, 9, 6, 6, 1],
    [8, 9, 3, 2, 3, 6],
    [8, 9, 3, 3, 9, 6]
]


def two_times_repeating_values(matrix):
    new_list = []

    for i in range(len(matrix)):
        counter = 0
        for j in range(len(matrix)):
            if i > j and i + j > len(matrix)-1:
                new_list.append(matrix[i][j])
    new_list.sort()

    counter = 0
    for i in range(len(new_list)-1):
        for j in range(i+1, len(new_list)):
            if new_list[i] == new_list[j]:
                counter += 1
        if counter != 2:
            new_list.remove(new_list[i])

    new_list = set(new_list)
    new_list = list(new_list)
    new_list.sort()

    return new_list
print(two_times_repeating_values(matrix2))

def test():
    assert two_times_repeating_values(matrix) == [3, 9]
    assert two_times_repeating_values(matrix2) == [3, 9] ##Issue here, it gives out of range with other matrix values
test()