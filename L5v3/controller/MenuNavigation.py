from L5v3.controller.CustomerController import add_new_customer, search_customer, update_customer, remove_customer
from L5v3.controller.DishController import remove_dish, update_dish, add_new_dish
from L5v3.controller.DrinkController import remove_drink, update_drink, add_new_drink
from L5v3.controller.OrderController import add_order
from L5v3.models.CookedDish import CookedDish
from L5v3.models.Drink import Drink
from L5v3.repository.CookedDishRepo import CookedDishRepo
from L5v3.repository.CustomerRepo import CustomerRepo
from L5v3.repository.DrinkRepo import DrinkRepo
from L5v3.repository.OrderRepo import OrderRepo
from L5v3.ui.CustommerControllerUI import add_new_customer_input
from L5v3.ui.RestaurantMenu import RestaurantMenu
from L5v3.ui.UserMenu import print_starting_menu


def main_menu(customerRepo: CustomerRepo, cookedDishRepo: CookedDishRepo, drinkRepo: DrinkRepo, orderRepo: OrderRepo):
    """
    central loop of the programme
    when this function stops, the whole program stops
    From here the user chooses what he wishes to do
    :param customerRepo: CustomerRepo with its filepath
    :param cookedDishRepo: CookedDishRepo with its filepath
    :param drinkRepo: DrinkRepo with its filepath
    :param orderRepo: OrderRepo with its filepath
    Their paths are given in app.py
    """
    while True:
        customers = customerRepo.load()
        dishes = cookedDishRepo.load()
        drinks = drinkRepo.load()
        orders = orderRepo.load()

        restaurant_menu = RestaurantMenu(dishes, drinks)

        print_starting_menu()

        option = int(input("Enter your desired option from the list: ").strip())
        print("\n")

        if option == 1:
            print(restaurant_menu)

        elif option == 2:
            add_order(orders, dishes, drinks, customers)

        elif option == 3:
            print("Specify the details of the dish you want to add")
            try:

                name = input("Enter a new name for your cooked dish: ").strip()
                portion_size = int(input("Enter a new value for the portion size of your cooked dish: ").strip())
                price = int(input("Enter a new value for the price of your cooked dish: ").strip())
                prep_time = int(input("Enter a new value for the preparation time of your cooked dish: ").strip())

                new_dish = CookedDish(name=name, portion_size=portion_size, price=price, prep_time=prep_time)

            except:
                continue

            add_new_dish(dishes, new_dish)

        elif option == 4:
            update_dish(dishes)

        elif option == 5:
            remove_dish(dishes)

        elif option == 6:
            print("Specify the details of the drink you want to add")
            try:

                name = input("Enter a new name for your drink: ").strip()
                portion_size = int(input("Enter a new value for the portion size of your drink: ").strip())
                price = int(input("Enter a new value for the price of your drink: ").strip())
                alcohol = int(input("Enter a new value for the alcohol content of your drink: ").strip())

                new_drink = Drink(name=name, portion_size=portion_size, price=price, alcohol=alcohol)
            except:
                continue

            add_new_drink(drinks, new_drink)

        elif option == 7:
            update_drink(drinks)

        elif option == 8:
            remove_drink(drinks)

        elif option == 9:
            customer = add_new_customer_input()
            customers = add_new_customer(customers, customer)

        elif option == 10:
            print("Search for your desired customer that you want to update" + "\n")
            customer = search_customer(customers)

            if customer is None:
                continue

            name = input("Enter a new name for your customer: ").strip()
            address = input("Enter a new address for your customer: ").strip()

            if name == "":
                name = None

            if address == "":
                address = None

            update_customer(customers, customer, name, address)

        elif option == 11:
            print("Search for your desired customer that you want to remove" + "\n")
            customer = search_customer(customers)

            if customer is None:
                continue

            remove_customer(customers, customer)

        elif option == 12:
            return
        else:
            pass

        customerRepo.save(customers)
        cookedDishRepo.save(dishes)
        drinkRepo.save(drinks)
        orderRepo.save(orders)
