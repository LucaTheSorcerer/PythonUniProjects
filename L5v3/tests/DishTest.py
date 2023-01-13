from models.CookedDish import CookedDish
from repository.CookedDishRepo import CookedDishRepo

"""
Here we test the functionalities of the DishRepo class
"""


def add_dish_test():
    repo = CookedDishRepo("dishes.txt")
    dish = CookedDish(0, "Telemea", 450, 12, 15)
    # print(dish)
    repo.save([dish])

    read_dish = repo.load()[0]
    assert dish == read_dish


add_dish_test()
