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


def ub1(greatest = False):
    with open("zahlen.txt") as f:
        content = f.readlines()
        lines = list(map(lambda line: line.strip("\n").split("\t"), content))

        numbers = list(map(lambda line: list(map(lambda string: int(string), line)), lines))

        print(numbers)

        #generate list of maximum and a list of minimum of the numbers from each list
        if greatest:
            max_list = list(map(lambda numbers_list: reduce(lambda number1, number2: max(number1, number2), numbers_list), numbers))
            print(max_list)
            product = reduce(lambda number1, number2: number1 * number2, max_list)
            print(product)
        else:
            min_list = list(map(lambda numbers_list: reduce(lambda number1, number2: min(number1, number2), numbers_list), numbers))
            print(min_list)
            product = reduce(lambda number1, number2: number1 * number2, min_list)

        return product

def correct_test():
    assert ub1(True) == 175587750

def incorrect_test():
    try:
        assert ub1() == 2
    except AssertionError:
        print("Incorrect")

def test():
    correct_test()
    incorrect_test()
test()

def main():
    print(ub1(True))
main()