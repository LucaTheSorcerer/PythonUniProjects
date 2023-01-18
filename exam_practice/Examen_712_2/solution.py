"""
Aufgabe 1
"""
# 1. a. Geben sei eine Textdatei mit dem Namen "my_file.txt" an, die in jeder Zeile den Vor- und Nachnamen des
# Schülers, das Fach und die jeweilige Note enthält, getrennt durch drei Leerzeichen ("   "), schreiben Sie eine
# Funktion namens "ub1", die:
# - einen Parameter namens "uppercase" erhält
# - aus der angegebenen CSV-Datei
# "my_file.txt" liest
# - wenn "uppercase" der Wert "True" (bool) hat, behalten nur die Zeilen, in denen der Nachname
# mit einem Großbuchstaben beginnt (0.25p)
# - wenn "uppercase" der Wert "False" (bool) hat, behalten nur die Zeilen,
# in denen der Nachname mit einem Kleinbuchstaben beginnt (0.25p)
# - Das Ergebnis der Funktion ist eine Zeichenkette,
# die aus den Fächern der behaltenen Zeilen, zusammengefügt mit dem "|" Zeichen, aufgebaut ist. (0.5p)
# Es sind keine
# for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und andere
# mathematische Operationen, falls erforderlich, benützt sind. (2p)

# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.

from functools import reduce

def ub1(uppercase = False):
    with open("text.txt") as f:
        content = f.readlines()

    content = map(lambda x : x.strip("\n"), content)
    content = list(map(lambda lines: lines.split("   "), content))

    if uppercase:
        content = list(filter(lambda name : name[1][0].isupper(), content))

    else:
        content = list(filter(lambda name: not name[1][0].isupper(), content))

    subjects = list(map(lambda subject: subject[-2], content))

    content = reduce(lambda subject1, subject2: subject1 + " | " + subject2, subjects)

    return content

def correct_test():
    assert ub1(True) == "Fundamentals of programming | Advanced programming | Advanced programming | Advanced programming | Advanced programming"

def incorrect_test():
    try:
        assert ub1(False) == "Fundamentals of programming | Advanced programming | Advanced programming | Advanced programming | Advanced programming"
    except:
        raise AssertionError("Incorrect assert")



# 2. a. Schreiben Sie die Definition für eine Klasse namens "TodoList". Die Klasse sollte in der Lage sein,
# das Folgende zu tun: - bei der Initialisierung wird die Instanzvariable "todos" auf eine leere Liste und die
# Instanzvariable "name" auf einen gegebenen Parameter gesetzt. (0.5p) - eine Methode namens "done" haben,
# die: - einen einzelnen string Parameter bekommt - prüft, ob der Parameter sich in der "todos" befindet (0.5pp) -
# falls gefunden, entfern es von "todos" und gibt als Ergebnis den Index zurück, in dem der Parameter gefunden wurde
# (0.5p) - eine benutzerdefinierte Ausnahme namens "NotFound" wirft, wenn der Parameter in "todos" nicht gefunden
# wurde (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "ExtraTodoList", die von "TodoList" erbt. Die Klasse sollte
# folgendes können: - bei der Initialisierung setzt sie neben den Variablen von "TodoList" auch eine Instanzvariable
# namens "done_count" auf 0 (0.25p) - Überschreiben der Methode "done", um Folgendes zu tun: - Wiederverwendung der
# Methode "done" aus der Basisklasse (0.25) - Im Falle eines erfolgreichen Aufrufs wird das Ergebnis zurückgegeben
# und die Variable "done_count" um 1 inkrementiert. (0.25p) - im Falle einer fehlgeschlagenen Abhebung wird
# "done_count" um 1 dekrementiert (0.25p) - Die Summe zwischen zwei "ExtraTodoList" Instanzen (todo1+todo2) hat als
# Ergebnis eine neue "ExtraTodoList" Instanz und sein "todos" enthält die Elemente der jeweiligen Listen aus den
# anderen Instanzen. "done_count" wird auf die Summe der jeweiligen Werte aus den anderen Instanzen gesetzt(1p)

class NotFound(Exception):
    pass
class TodoList:
    def __init__(self, name):
        self.name = name
        self.todos = []


    def done(self, string):
        if string not in self.todos:
            raise NotFound("String not found!")

        else:
            index = self.todos.index(string)
            self.todos.remove(string)
            return index

class ExtraTodoList(TodoList):
    def __init__(self, name):
        super().__init__(name)
        self.done_count = 0

    def done(self, string):
        try:
            super().done(string)
            self.done_count += 1
        except NotFound:
            self.done_count -= 1

    def __add__(self, other):
        todo = ExtraTodoList(self.name)
        todo.todos = self.todos + other.todos
        todo.done_count = self.done_count + other.done_count

        return todo


"""
Aufgabe 3
"""
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n = n // 2
    return result


def recursive(x, n):
    result = 1
    if n == 0:
        return result
    return x * recursive(x, n-1)

def test():
    correct_test()
    #incorrect_test()
test()


def main():
    uppercase = True
    print(ub1(uppercase))
    print(my_func(2, 3))
    print(recursive(2, 3))
main()


