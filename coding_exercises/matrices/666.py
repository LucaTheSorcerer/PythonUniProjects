matrix = [
    [4, 20, 15, 23],
    [1, 8, 23, 22],
    [17, 15, 13, 23],
    [3, 18, 8, 20],
]


def isPrime(number):
    """
    This function checks whether the number is prime or not
    :param number: takes as input a variable that represent each number or element of the matrix
    :return: returns True if the number is prime, False otherwise
    """
    if number == 1 or number == 0:
        return False
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True


def prime_numbers_on_even_lines(matrix):
    """
    This function checks whether each element of the matrix is a prime number or not and increments
    the counter if the number is prime
    :param matrix: takes as input a matrix or a list of nested lists
    :return: returns the counter of the prime numbers of the matrix
    """
    counter = 0
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix)):
                if isPrime(matrix[i][j]):
                    counter += 1
    return counter


print(prime_numbers_on_even_lines(matrix))


def test_for_isPrime():
    """
    This test checkss the test_for_isPrime function
    :return:
    """
    assert isPrime(13)
    assert not isPrime(4)


test_for_isPrime()


def test_for_prime_numbers_on_even_lines():
    """
    This test checkss the test_for_prime_numbers_on_even_lines function
    :return:
    """
    assert prime_numbers_on_even_lines(matrix) == 4
    assert not prime_numbers_on_even_lines(matrix) == 5


test_for_prime_numbers_on_even_lines()
