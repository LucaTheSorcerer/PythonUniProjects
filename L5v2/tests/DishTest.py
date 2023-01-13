from L5v2.models.CookedDish import CookedDish
from L5v2.repository.CookedDishRepo import CookedDishRepo

"""
Test for DishRepo class
"""

def add_dish_test():
    repo = CookedDishRepo("dishes.txt")
    dish = CookedDish(0, "Telemea", 450, 12, 15)
    repo.save([dish])

    read_dish = repo.load()[0]
    assert dish == read_dish

add_dish_test()