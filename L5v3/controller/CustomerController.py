from models.Customer import Customer
from ui.CustommerControllerUI import search_customer_prints


def add_new_customer(customers: list[Customer], customer: Customer):
    """
    :param customer: The customer to be appended to the list
    :param customers: a list of customers
    :return: The appended list
    """
    customers.append(customer)

    return customers


def search_customer(customers: list[Customer]):
    """
    This function searches for a specific customer in the list
    :param customers: A list of customer
    :return: A customer
    """
    search_customer_prints()
    try:
        option = int(input("Your option ").strip())
    except:
        return

    if option == 1:
        address = input("Address: ").strip()
        tempCustomers = search_customer_by_address(customers, address)
    elif option == 2:
        name = input("Name: ").strip()
        tempCustomers = search_customer_by_name(customers, name)
    else:
        print("Invalid option")
        return

    if tempCustomers is None:
        print("No customer was found, try again")
        return None

    for i in range(len(tempCustomers)):
        print(f"Index: {i}, Customer: {tempCustomers[i]}")

    try:
        option = int(input("Choose the index of the customer you want ").strip())
        return tempCustomers[option]
    except IndexError:
        return None


def search_customer_by_address(customers: list[Customer], address: str):
    """
    It is obvious from its name what this function does
    """
    result = list(filter(lambda customer: address.lower() in customer.address.lower(), customers))

    return result


def search_customer_by_name(customers: list[Customer], name: str):
    """
    It is obvious from its name what this function does
    """
    result = list(filter(lambda customer: name.lower() in customer.name.lower(), customers))

    return result


def update_customer(customers: list[Customer], customer: Customer, name=None, address=None):
    """
    Updates a customer with new properties
    """
    index = customers.index(customer)
    if name is not None:
        customers[index].name = name
    if address is not None:
        customers[index].address = address
    return customers


def remove_customer(customers: list[Customer], customer: Customer):
    """
    Removes a customer from the list
    """
    customers.remove(customer)
    return customers
