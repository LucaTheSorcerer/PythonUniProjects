from L5v2.models.CookedDish import CookedDish
from L5v2.repository.CookedDishRepo import CookedDishRepo
from L5v2.repository.DrinkRepo import DrinkRepo
from L5v2.ui.RestaurantMenu import RestaurantMenu

"""
This tests the functionality of the generated menu
"""

def test_generate_menu():
    dish_repo = CookedDishRepo("dishes.txt")
    drink_repo = DrinkRepo("drinks.txt")