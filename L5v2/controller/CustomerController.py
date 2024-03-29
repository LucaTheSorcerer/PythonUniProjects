from L5v2.models.Customer import Customer
from L5v2.ui.CustomerControllerUI import search_customer_prints

def add_new_customer(customers: list[Customer], customer: Customer):
    """
    :param customers: a list of customers
    :param customer: a customer to be added
    :return: the list with customers
    """
    customers.append(customer)

    return customers

def search_customer(customers: list[Customer]):
    """
    searches for a customer in the list
    :param customers: list of customers
    :return: customer
    """
    search_customer_prints()

    try:
        option = int(input("Your option: ").strip())
    except:
        return

    if option == 1:
        address = input("Address: ").strip()
        tempCustomers = search_customer_by_address(customers, address)
    elif option == 2:
        name = input("Name: ").strip()
        tempCustomers = search_customer_by_name(customers, name)
    else:
        print("Invalid Option")
        return

    if tempCustomers is None:
        print("No customer has been found, try again!")
        return None

    for i in range(len(tempCustomers)):
        print(f"Index: {i}, Customer: {tempCustomers[i]}")

    try:
        option = int(input("Choose the index of your desired customer: ").strip())
        return tempCustomers[option]
    except IndexError:
        return None

def search_customer_by_address(customers: list[Customer], address: str):
    """
    Searches a customer by its address
    """
    result = list(filter(lambda customer: address.lower() in customer.address.lower(), customers))
    return result

def search_customer_by_name(customers: list[Customer], name : str):
    """
    Searches a customer by its name
    """
    result = list(filter(lambda customer: name.lower() in customer.name.lower(), customers))
    return result

def update_customer(customers: list[Customer], customer: Customer, name = None, address = None):
    """
    Updates the name and the address of a customer
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