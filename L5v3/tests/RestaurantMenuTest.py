from L5v3.models.CookedDish import CookedDish
from L5v3.repository.CookedDishRepo import CookedDishRepo
from L5v3.repository.DrinkRepo import DrinkRepo
from L5v3.ui.RestaurantMenu import RestaurantMenu

"""
Tests the menu and checks if its successfully generated
"""


def test_generate_menu():
    dish_repo = CookedDishRepo("dishes.txt")
    drinks_repo = DrinkRepo("drinks.txt")

    dishes = [CookedDish(0, "Pizza", 450, 12, 15), CookedDish(1, "Ciorba de burta", 350, 24, 45)]
    dish_repo.save(dishes)
    drinks = drinks_repo.load()
    menu = RestaurantMenu(dishes, drinks)

    # print(menu)

    assert "Pizza" in str(menu) and "Ciorba de burta" in str(menu) and "Vodka" in str(menu)


test_generate_menu()
