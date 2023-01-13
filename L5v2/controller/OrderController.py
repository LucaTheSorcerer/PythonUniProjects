from L5v2.controller.CustomerController import search_customer
from L5v2.models.Customer import Customer
from L5v2.models.Dish import Dish
from L5v2.models.Drink import Drink
from L5v2.models.Order import Order

def add_order(orders, dishes, drinks, customers):
    """
    handles all about an order
    :param orders: list of orders
    :param dishes: list of dishes
    :param drinks: list of drinks
    :param customers: list of customers
    """
    customer = search_customer(customers)

    if customer is None:
        print("Add the customer to the list")
        return

    dish_IDs = []
    drink_IDs = []

    while True:
        print("Press 1 to add a dish")
        print("Press 2 to add a drink")
        print("Press 3 to finish the order")
        print("Press 4 to se the current time in the order")
        print("Press 5 to exit")

        option = int(input("Enter your option: "))

        if option == 1:
            for i in range(len(dishes)):
                print(f"Index: {i}, Dish: {str(dishes[i])}")

            try:
                option = int(input("Choose the index of the drink you want to add: "))

                if option not in range(len(dishes)):
                    continue

                dish_IDs.append(dishes[option].id)

            except:
                continue

        elif option == 2:
            for i in range(len(drinks)):
                print(f"Index: {i}, Drink: {str(drinks[i])}")

            try:
                option = int(input("Choose the index of the drink you want to add"))

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
    print(f"Estimated waiting time for the order is: {order.generate_estimated_wait_time(dishes)}")