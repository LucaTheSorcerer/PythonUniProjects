def read_from_file():
    with open("tiban.txt") as f:
        return f.read().split("\n")


def join_from_file():
    return " ".join(read_from_file())


print(read_from_file())
print(join_from_file())
