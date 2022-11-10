def reverse_File():
    with open("challenge.txt") as f:
        data = f.read()
        data = data[::-1]

    f = open("challenge.txt", "w")
    f.write(data)
    print(data)
reverse_File()

n = 10
print( all(n % i == 0 for i in range(2, int(n**.5)+1)))
