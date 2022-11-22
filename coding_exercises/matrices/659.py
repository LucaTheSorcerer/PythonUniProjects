matrix = [
    [5, 5, 10, 5],
    [3, 9, 1, 9],
    [4, 10, 1, 2]
]

def sum_line_without_maxel(matrix):
    list1 = []
    for i in range(len(matrix)):
        sum_every_line = 0
        max_element = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
            sum_every_line += matrix[i][j]
        sum_every_line -= max_element
        list1.append(sum_every_line)
    return list1
print(sum_line_without_maxel(matrix))
