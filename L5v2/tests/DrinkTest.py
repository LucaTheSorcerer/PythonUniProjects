from L5v2.models.Drink import Drink
from L5v2.repository.DrinkRepo import DrinkRepo

"""
This tests the functionalities of the DrinkRepo class
"""

def add_drink_test():
    repo = DrinkRepo("drinks.txt")
    drink = Drink(0, "Sprite", 450, 120, 95)

    repo.save([drink])
    read_drink = repo.load()[0]
    assert drink == read_drink

add_drink_test()