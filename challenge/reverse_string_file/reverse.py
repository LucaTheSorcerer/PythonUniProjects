def reverse_File():
    with open("challenge.txt") as f:
        data = f.read()
        data = data[::-1]

    f = open("challenge.txt", "w")
    f.write(data)
    print(data)
reverse_File()