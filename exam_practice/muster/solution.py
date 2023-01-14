"""
Aufgabe 1
"""



"""
Aufgabe 2
"""
class Cartrdige:
    def __init__(self, tintestand, farbe):
        self.tintestand = tintestand
        self.farbe = farbe

class Printer:
    def __init__(self):
        self.cartridges = []

    def add_cartridge(self, cartridge):
        if cartridge.tintestand == 0:
            raise RuntimeError("Cannot add empty Cartridge")

        if len(self.cartridges) > 3:
            raise RuntimeError("Printer can only contain three cartridges at a time")

        for ce in self.cartridges:
            if ce.farbe == cartridge.farbe and ce.tinestand > 0:
                raise RuntimeError("Only replace emppty cartridges")

        self.cartridges.append(cartridge)


    def remove_cartridge(self, color):
        for cartridge in self.cartridges:
            if cartridge.farbe == color:
                self.cartridges.remove(cartridge)
                return
        raise RuntimeError("No cartridge found!")

    def print(self, liste, file_path = "exam_practice/muster/test1.txt"):
        f = open(file_path, "w")

        for line in liste:
            f.write(line + "\n")

        f.close()

class SmartPrinter(Printer):
    def __init__(self):
        super().__init__()

    def print(self, liste, file = "exam_practice/muster/test1.txt"):
        super().print(liste, file)

        n = len("".join(liste))

        print(f"Printed a document of length {n} to path {file}")

def check():
    cartridge1 = Cartrdige(50, 'rot')
    cartridge2 = Cartrdige(70, 'blau')

    cartridge3 = cartridge1 + cartridge2

    assert isinstance(cartridge3, Cartrdige)
    assert cartridge3 is not cartridge1
    assert cartridge3.farbe == 'rotblau'
    assert cartridge3.tintenstand == 100
check()
