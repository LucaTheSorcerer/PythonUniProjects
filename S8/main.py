"""
overloading = mehrere Methoden mit dem gleichen Namen aber unterschiedliche Parameteranzahl
overriding = mehrere Metyhoden mit dem gleichen Namen unde den gleichen Parametereanzahl
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f'{self.name} is sleeping... ')

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        """
        self.name = bob in exemplul nostru
        self.other = bobby in exemplul nostry
        :param other:
        :return:
        """
        return self.name == other.name and self.age == other.age


class Student(Person):
    """
    die Klasse Student vererbt alle Methoden und Attribute der Klasse Person
    aber kann auch weitere Methoden definieren und implementieren

    Person = Bassisklasse, Oberklasse, Superklasee
    Student = Unterklasse

    Vererbung is eine is-a Bezeihung zwischen 2 Klassen -
        ein Student ist einfach EINE PERSON
    """

    def __init__(self, name, age, uni):
        super().__init__(name, age) #man ruft die __init__ Methode der Bassisklasse
        self.uni= uni


    def study(self):
        print(f'{self.name} is studying... ')

    #overloading
    def study(self, faecher):
        print(f'{self.name} is studying for {faecher}... ')

    """
    A doua metoda study o suprascrie pe prima
    """

    #overriding
    def sleep(self):
        print(f'{self.name} cannot sleep, must study...')


def main():
    bob = Person('bob', 20)
    bob.sleep()

    dob = Student('dob', 20, 'ubb')
    dob.study('OOP,....')
    #dob.study()
    dob.sleep()

    print(bob)

    bobby = Person('bobby', 21)

    print(bob == bobby)

    bobby = Person('bob', 20)
    print(bob == bobby) #bob.__eq__(bobby) ==> bob = self, bobby = other



main()