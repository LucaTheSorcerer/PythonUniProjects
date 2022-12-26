from functools import reduce

n = 20

fibonacci = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0,1])

print(fibonacci)