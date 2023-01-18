from functools import reduce


def read_file():
    # Read the contents of the file
    with(open("my_file.txt") as f):
        content = f.read()

        # Use repeated splits on the content of the file to transform the string in to a matrix of strings
        content = content.split("\n")
        return list(map(lambda x: x.split("   "), content))


# print(read_file())


def ub1(uppercase=False):
    content = read_file()

    if uppercase:
        # Wir behalten die gross geschriebenen Nachnamen
        content = list(filter(lambda x: (x[1][0].isupper()), content))
    else:
        # Wir behalten die klein geschriebenen Nachnamen
        content = list(filter(lambda x: not (x[1][0].isupper()), content))

    # Wir behalten nur die Facher
    content = list(map(lambda x: x[-2], content))

    # Remove duplicates from content
    content = list(dict.fromkeys(content))

    # content = "|".join(content)

    # Wir wiedergeben die Facher als einen einzigen String
    content = reduce(lambda s, x: s + '|' + x, content)

    return content


print(ub1(True))
print(ub1())


def test_ub1():
    # Wir testen den output der function ub1() wenn uppercase ist Falsch
    assert ub1() == "Advanced programming|Vocal Training|Acting 101"

    try:
        # Wir testen, ob die Function ub(1) mit uppercase falsch 1 wiedergibt und das
        # kann nie wahr sein, da ein string nie gleich zu einem int sein kann
        assert ub1() == 1
    except AssertionError:
        print("The function works as intended")


test_ub1()
