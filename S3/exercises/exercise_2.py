a = "1212312231231"
b = "5553412313231"

def big_sum(string1, string2):
    """
    This function takes as input two strings made of numbers and returns the sum of
    the two strings in another string
    :param string1: paramter for the first string
    :param string2: parameter for the second string
    :return: return the result after the sum
    """
    result = ' '
    for i in range(len(string1)-1, -1, -1):
        cif = int(string1[i]) + int(string2[i])
        carry = cif // 10
        result = str(cif % 10 + carry) + result
    if carry > 0:
        result = str(carry) + result
    return result
print(big_sum(a, b))