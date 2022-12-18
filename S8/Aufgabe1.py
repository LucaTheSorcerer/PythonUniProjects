class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating... ')

class Pig(Animal):
    def __init__(self, name, age):
        super().__init__(name)

        self.age = age

    def sleep(self):
        print(f'{self.name} is sleeping... ')

class Chicken(Animal):
    def __init__(self, color, name):
        super().__init__(name)

        self.color = color


class Farm:
    def __init__(self, animals, name, city):
        self.animals = animals
        self.name = name
        self.city = city

    def feedAnimals(self):
        for animal in self.animals:
            animal.eat()


def main():
    farm = Farm([Pig('bob', 4), Chicken('red', 'dob')], 'Cluj-Farm', 'cluj')
    farm.feedAnimals()
main()