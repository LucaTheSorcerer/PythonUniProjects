a = "1234556544345"
b = "2343234"

def big_sum_different_numbers_length(string1, string2):
    result = ""
    fill = "0" * abs((len(string1) - len(string2)))

    if len(string1) > len(string2):
        string2 = fill + string2
    if len(string2) > len(string1):
        string1 = fill + string1

    for i in range(len(string1)-1, -1, -1):
        cif = int(string1[i]) + int(string2[i])
        carry = cif // 10
        result = str(cif % 10 + carry) + result

    if carry > 0:
        result = str(carry) + result
    return result
print(big_sum_different_numbers_length(a, b))