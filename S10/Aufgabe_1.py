def sum_all_ziffer(number):
    sum = 0
    if number == 0:
        return 0

    c = number % 10
    return (c if c % 2 == 0 else 0) + sum_all_ziffer(number//10)
    # if c % 2 == 0:
    #     return c%10 + sum_all_ziffer(number//10)
    # else:
    #     return sum_all_ziffer(number//10)

print(sum_all_ziffer(12354))


lambda number: number