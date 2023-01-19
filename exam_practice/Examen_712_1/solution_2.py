"""
Aufgabe 2
"""
# 2. a. Schreiben Sie die Definition für eine Klasse namens "DecryptedText". Die Klasse sollte in der Lage sein,
# das Folgende zu tun: - bei der Initialisierung wird die Instanzvariable "characters" auf einen gegebenen Parameter
# gesetzt. Der Typ des Parameters ist eine Liste von Zeichen. (0.5p) - eine Methode namens "encrypt" haben,
# die: - für alle Zeichen aus der Liste "characters" prüft, dass sich alle im Interval "a-z" sich befindet (0.5pp) -
# gibt eine Liste mit den konvertierten Zeichen in Zahlen zurück, die die ASCII-Tabelle verwenden (0.5p) - eine
# benutzerdefinierte Ausnahme namens "UnacceptedValue" wirft, wenn ein Zeichen nicht im Interval befindet (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "ActualDecryptedText", die von "DecryptedText" erbt. Die
# Klasse sollte folgendes können: - bei der Initialisierung setzt sie neben den Variablen von "CaesarDecryptedText"
# auch eine Instanzvariable namens "numbers" auf None Wert (0.25p) - Überschreiben der Methode "decrypt",
# um Folgendes zu tun: - Wiederverwendung der Methode "decrypt" aus der Basisklasse (0.25) - Im Falle eines
# erfolgreichen Aufrufs wird das Ergebnis zurückgegeben und im Instanzvariable "numbers" gespeichert (0.25p) - im
# Falle einen fehlgeschlagenen Aufruf wird die Instanzvariable "numbers" auf leere Liste gesetzt (0.25p) - Das
# Ergebnis der Addition zwischen einer Instanz des Typs "ActualDecryptedText" und einer Zahl (instanz + 3) ist eine
# neue Instanz des Typs "ActualDecryptedText", die die Elemente aus "numbers" um die Zahl (aus der Addition) erhöht.
# (1p)

class UnacceptedValue(Exception):
    pass

class DecryptedText:
    def __init__(self, characters: list[str]):
        self.characters = characters

    def encrypt(self):
        ascii_list = []
        for character in self.characters:
            if not character.islower():
                raise UnacceptedValue
            else:
                ascii_list.append(ord(character))
        return ascii_list

class ActualDecryptedText(DecryptedText):
    def __init__(self, characters):
        super().__init__(characters)
        self.numbers = None

    def encrypt(self):
        try:
            #super().encrypt()
            self.numbers = super().encrypt()
        except UnacceptedValue:
            self.numbers = []

    def __add__(self, other):
        new_instance = ActualDecryptedText(self.characters)
        new_instance.encrypt()

        for i in range(len(new_instance.numbers)):
            new_instance.numbers[i] += other

        return new_instance

def main():
    d = DecryptedText(['a', 'b', 'c'])
    print(d.encrypt())

    c1 = ActualDecryptedText(['a', 'b', 'c'])
    c2 = c1 + 3
    print(c2.numbers)
main()
