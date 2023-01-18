"""
Aufgabe 1
"""
# 1.
# a. Geben sei eine Textdatei mit dem Namen "text.txt" an, die in jeder Zeile den Namen des Schülers, das Fach und
# die jeweilige Note enthält, getrennt durch zwei Leerzeichen ("  "), schreiben Sie eine Funktion namens "ub1", die:
# 	- aus der angegebenen CSV-Datei "text.txt" liest
# 	- nur die Zeilen behält, die die Note größer als 8 haben (0.5p)
# 	- die Summe der Noten, der behaltenen Zeilen, berechnet und das Ergebnis zurückgibt (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.

def ub1():
    with open("text.txt") as f:
        data = f.readlines()


    lines = list(map(lambda line: line.split(" "),map(lambda line: line.strip(), data)))

    desired_lines = list(filter(lambda note : int(note[-1]) >= 8, lines))

    notes = list(map(lambda note: int(note[-1]), desired_lines))

    sum_notes = sum(notes)

    return sum_notes

def correct_test_ub1():
    assert ub1() == 29

def incorrect_test_ub1():
    try:
        assert ub1() == 5
    except AssertionError:
        print("The error is here")

def testing():
    correct_test_ub1()
    incorrect_test_ub1()
testing()

# def read_file():
#     with open("text.txt") as f:
#         data = f.read()
#
#         data = data.split("\n")
#         return list(map(lambda line: line.split(" "), data))



"""
Aufgabe 2
"""
# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "DebitCard".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
# 	 - bei der Initialisierung die Instanzvariable "money" auf 0 und die Instanzvariable "name" auf einen
# 	   gegebenen Parameter setzen (0.5p)
# 	 - eine Methode namens "pay" haben, die:
# 	 	- einen einzelnen ganzzahligen Parameter bekommt
# 	 	- prüft, ob der Parameter größer oder gleich der Variablen "money" ist (0.5pp)
# 	 	- die Differenz zwischen dem "money" und dem gegebenen Parameter zurückgibt und als neue Wert für "money" speichert (0.5p)
# 	 	- eine benutzerdefinierte Ausnahme namens "NoBalance" wirft, wenn der Parameter größer als "money" ist (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "CreditCard", die von "DebitCard" erbt.
#  Die Klasse sollte folgendes können:
# 	- bei der Initialisierung setzt sie neben den Variablen von "DebitCard" auch eine Instanzvariable namens
#  	  "debt" auf 0 (0.25p)
# 	- Überschreiben der Methode "pay", um Folgendes zu tun:
# 		- Wiederverwendung der Methode "pay" aus der Basisklasse (0.25)
# 		- im Falle einer erfolgreichen Abhebung wird das Ergebnis zurückgegeben (0.25p)
# 		- im Falle einer fehlgeschlagenen Abhebung wird ganzzahligen Parameter von der "pay" Methode zum "debt" addiert (0.25p)
# 	- Die Multiplikation zwischen ein "CreditCard" Instanz und eine Zahl (credit_card * 3) hat als Ergebnis
#     eine Liste von "CreditCard" instanzen die der gleiche Zustand der originalen Instanz haben. Die länge der Liste
#     ist gleich mit der Zahl aus der Multiplikation (1p)


class NoMoney(Exception):
    pass
class DebitCard:
    def __init__(self, name):
        self.name = name
        self.money = 0

    def pay(self, pay_amount):
        if pay_amount > self.money:
            raise NoMoney

        self.money -= pay_amount

        return self.money

class CreditCard(DebitCard):
    def __init__(self, name):
        super().__init__(name)
        self.debt = 0

    def pay(self, pay_amount):
        self.money -= pay_amount

        if pay_amount <= self.money:
            return self.money

        self.debt = self.money
        self.money = 0

    def __mul__(self, other):
        return [self for _ in range(other)]

"""
Aufgabe 3
"""
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def recursive(lst, x):

    if len(lst) == 0:
        return -1

    mid = len(lst) // 2

    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        return recursive(lst[mid + 1:], x)
    else:
        return recursive(lst[:mid], x)

def main():
    print(ub1())
    #print(read_file())

    debit = DebitCard("Luca")
    debit.money = 20
    print(debit.name, debit.money)
    print(debit.pay(10))

    credit = CreditCard("Alex")
    print(credit * 3)

    print(recursive([1, 2, 3, 4], 2))
    print(my_func([1, 2, 3, 4], 2))
main()

