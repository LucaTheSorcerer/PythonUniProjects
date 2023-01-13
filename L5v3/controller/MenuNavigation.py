from controller.CustomerController import add_new_customer, search_customer, update_customer, remove_customer
from controller.DishController import remove_dish, update_dish, add_new_dish
from controller.DrinkController import remove_drink, update_drink, add_new_drink
from controller.OrderController import add_order
from models.CookedDish import CookedDish
from models.Drink import Drink
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo
from ui.CustommerControllerUI import add_new_customer_input
from ui.RestaurantMenu import RestaurantMenu
from ui.UserMenu import print_starting_menu


def main_menu(customerRepo: CustomerRepo, cookedDishRepo: CookedDishRepo, drinkRepo: DrinkRepo, orderRepo: OrderRepo):
    """
    This is the central loop of the programme
    From here the user chooses what he wishes to do
    :param customerRepo: An instance of CustomerRepo with the appropriate filepath
    :param cookedDishRepo: An instance of CookedDishRepo with the appropriate filepath
    :param drinkRepo: An instance of DrinkRepo with the appropriate filepath
    :param orderRepo: An instance of OrderRepo with the appropriate filepath
    The paths are given at the entrypoint of the programme, app.py

    When this function ends, the programme ends
    """
    while True:
        customers = customerRepo.load()
        dishes = cookedDishRepo.load()
        drinks = drinkRepo.load()
        orders = orderRepo.load()

        restaurant_menu = RestaurantMenu(dishes, drinks)

        print_starting_menu()

        option = int(input("Your option: ").strip())
        print("\n")

        if option == 1:
            print(restaurant_menu)

        elif option == 2:
            add_order(orders, dishes, drinks, customers)

        elif option == 3:
            print("Specify the details of the dish you want to add")
            try:
                """
                I know this is stupid but i am tired
                """
                name = input("Enter a new name ").strip()
                portion_size = int(input("Enter a new portion size ").strip())
                price = int(input("Enter a new price ").strip())
                prep_time = int(input("Enter a new prep time ").strip())

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
                """
                I know this is stupid but i am tired
                """
                name = input("Enter a new name ").strip()
                portion_size = int(input("Enter a new portion size ").strip())
                price = int(input("Enter a new price ").strip())
                alcohol = int(input("Enter a new alcohol content ").strip())

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
            print("Search for the customer you want to update" + "\n")
            customer = search_customer(customers)

            if customer is None:
                continue

            name = input("Enter a new name: ").strip()
            address = input("Enter a new address: ").strip()

            if name == "":
                name = None

            if address == "":
                address = None

            update_customer(customers, customer, name, address)

        elif option == 11:
            print("Search for the customer you want to remove" + "\n")
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
