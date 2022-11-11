matrix = [
    [8, 3, 5, 6],
    [5, 5, 6, 5],
    [3, 8, 6, 5],
    [8, 4, 8, 8]
]

def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

def sum_above_and_under_first_diagonal(matrix):
    sum_above_first_diag = 0
    sum_under_first_diag = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < j:
                sum_above_first_diag += matrix[i][j]
            elif i > j:
                sum_under_first_diag += matrix[i][j]
    print(sum_above_first_diag)
    print(sum_under_first_diag)
    return gcd(sum_above_first_diag, sum_under_first_diag)
print(sum_above_and_under_first_diagonal(matrix))

