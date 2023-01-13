from L5v3.models.Drink import Drink
from L5v3.repository.DrinkRepo import DrinkRepo

"""
Tests the functionalities of the DrinkRepo class
"""


def add_drink_test():
    repo = DrinkRepo("drinks.txt")
    drink = Drink(0, "Vodka", 450, 120, 95)
    # print(drink)
    repo.save([drink])
    read_drink = repo.load()[0]
    assert drink == read_drink


add_drink_test()
