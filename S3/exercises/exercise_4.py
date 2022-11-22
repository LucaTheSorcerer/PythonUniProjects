matrix = [
    ['A', 'B', 'C', 'D'],
    ['L', 'E', 'G', 'H'],
    ['Q', 'R', 'T', 'F']
]

word =  "ALERT"
def find(elem):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if elem in matrix[i][j]:
                return i, j
        # if elem in matrix[i]:
        #     return i, matrix[i].index(elem)
    return -1, -1


"""
element1 = A --> i = 0, j = 0
element2 = L --> i = 1,  j = 0

"""
def neighbour(element1, element2):
    e1_i, e1_j = find(element1)
    e2_i, e2_j = find(element2)

    if (e1_i == e2_i) and (e1_j == e2_j + 1) or (e1_j == e2_j - 1):
        return True

    if (e1_j == e2_j) and (e1_i == e2_i + 1) or (e1_i == e2_i - 1):
        return True
    return False
def solution_exists(word):
    for i in range(1, len(word)):
        if not neighbour(word[i-1], word[i]):
            return False
    if not neighbour(word[-1], word[-2]):
        return False
    return True
print(solution_exists(word))