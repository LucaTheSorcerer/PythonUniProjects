from controller.CustomerController import search_customer
from models.Customer import Customer
from models.Dish import Dish
from models.Drink import Drink
from models.Order import Order


def add_order(orders: list[Order], dishes: list[Dish], drinks: list[Drink], customers: list[Customer]):
    """
    :param orders: A list of all orders
    :param dishes: A list of all dishes
    :param drinks: A list of all drinks
    :param customers: A list of all customers
    This function handles everything there is about orders
    """

    customer = search_customer(customers)

    if customer is None:
        print("Try adding the customer in the list")
        return

    dish_IDs = []
    drink_IDs = []

    while True:
        print("Press 1 to add a dish")
        print("Press 2 to add a drink")
        print("Press 3 to finish the order")
        print("Press 4 to see the current items in the order")
        print("Press 5 to exit")

        option = int(input("Your option: "))

        if option == 1:
            for i in range(len(dishes)):
                print(f"Index: {i}, Dish: {str(dishes[i])}")

            try:
                """
                I know this is stupid but i am tired
                """

                option = int(input("Choose the index of the drink you want to update "))

                if option not in range(len(dishes)):
                    continue

                dish_IDs.append(dishes[option].id)
            except:
                continue
        elif option == 2:
            for i in range(len(drinks)):
                print(f"Index: {i}, Drink: {str(drinks[i])}")

            try:
                """
                I know this is stupid but i am tired
                """

                option = int(input("Choose the index of the drink you want to update "))

                if option not in range(len(drinks)):
                    continue

                drink_IDs.append(drinks[option].id)
            except:
                continue

        elif option == 3:
            break
        elif option == 4:
            print(dish_IDs)
            print(drink_IDs)
        elif option == 5:
            return
        else:
            pass

    order = Order(customer_id=customer.id, drinks_ids=drink_IDs, dish_ids=dish_IDs)
    orders.append(order)
    print(order)

    order.show_bill(dishes, drinks)
    print(f"Estimated wait Time for the order {order.generate_estimated_wait_time(dishes)}")
