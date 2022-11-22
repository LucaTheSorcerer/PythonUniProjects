class Auto:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

class Statistics:
    def __init__(self):
        self.autos = []

    def add_auto(self, auto):
        self.autos.append(auto)

    def anzahl_auto_farbe(self, color):
        anzahl = 0
        for auto in self.autos:
            if auto.color == color:
                anzahl += 1

        return  anzahl

    def avg_baujahr(self, brand):
        sum = 0
        year = 0
        nr = 0
        for auto in self.autos:
            if auto.brand == brand:
                year += auto.year
                nr += 1
        return year / nr

def main():
    ford1 = Auto("Ford", "Mustang", 2010, "blue")
    ford2 = Auto("Ford", "Mustang1", 2005, "green")
    mercedes = Auto("Mercedes", "G-Class", 2011, "green")
    stats = Statistics()
    stats.add_auto(ford1)
    stats.add_auto(ford2)

    print(stats.anzahl_auto_farbe('blue'))
    print(stats.avg_baujahr(2010))
main()