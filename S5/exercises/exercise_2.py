

def check_for_evey_line_diagonal(matrix):
    result = []
    for i in range(len(matrix)):
        sum_line = 0
        for j in range(len(matrix)):
            if i != j:
                sum_line += matrix[i][j]

        result.append(sum_line == matrix[i][i])

    return result

def main():
    global matrix
    matrix = [
        [4, 3, 1],
        [1, 2, 1],
        [0, 5, 1]
    ]

    diagonals = check_for_evey_line_diagonal(matrix)
    print(diagonals)
main()

def test():
    assert check_for_evey_line_diagonal(matrix) == [True, True, False]
    #assert check_for_evey_line_diagonal(matrix) == [False, False, True]
test()

