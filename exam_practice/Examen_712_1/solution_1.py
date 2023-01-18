"""
Aufgabe 1
"""
from functools import reduce


# 1.
# a. Geben sei eine Textdatei mit dem Namen "zahlen.txt" an, auf eine mehreren Zeilen, Zahlen die durch
# ein Tab-Zeichen "\t" getrennt sind.
# schreiben Sie eine Funktion namens "ub1", die:
#   - einen Parameter namens "greatest" erhält
# 	- aus der angegebenen CSV-Datei "zahlen.txt" liest
# 	- wenn "greatest" der Wert "True" (bool) hat, für jede Zeile, behaltet man nur die größte Zahl (0.25p)
# 	- wenn "greatest" der Wert "False" (bool) hat, für jede Zeile, behaltet man nur die niedrigste Zahl (0.25p)
# 	- Das Ergebnis der Funktion ist die Multiplikation aller behaltenen Zahlen (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.


def read_from_file():
    with open("zahlen.txt") as f:
        content = f.readlines()

    lines = list(map(lambda lines : lines.strip("\n").split("\t"), content))

    numbers = list(map(lambda line: list(map(lambda string: int(string), line)), lines))

    return numbers

print(read_from_file())
def ub1(greatest = True):

    content = read_from_file()

    if greatest:
        #generates the maximum number from each list and stores it into a list
        max_list = list(map(lambda numbers_list: reduce(lambda a, b: max(a, b), numbers_list), content))

        product = reduce(lambda number1, number2: number1 * number2, max_list)

    else:
        #generates the minimum number from each list and stores it into a list
        min_list = list(map(lambda numbers_list: reduce(lambda number1, number2: min(number1, number2), numbers_list), content))
        product = reduce(lambda number1, number2: number1 * number2, min_list)

    return product


def correct_test():
    assert ub1() == 25 * 29 * 27 * 26 * 15 * 23

def incorrect_test():
    try:
        assert ub1() == 1 * 3
    except AssertionError:
        print("Not working!")

def tests():
    correct_test()
    incorrect_test()
tests()
def main():
    print(ub1())
main()