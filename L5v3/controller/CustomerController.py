from L5v3.models.Customer import Customer
from L5v3.ui.CustommerControllerUI import search_customer_prints


def add_new_customer(customers: list[Customer], customer: Customer):
    """
    :param customer: The customer to be appended to the list
    :param customers: list of customers
    :return: The appended list
    """
    customers.append(customer)

    return customers


def search_customer(customers: list[Customer]):
    """
    This function searches for a specific customer in the list
    :param customers: list of customer
    :return: customer
    """
    search_customer_prints()
    try:
        option = int(input("Please enter your desired option ").strip())
    except:
        return

    if option == 1:
        address = input("Enter the Address of the customer: ").strip()
        tempCustomers = search_customer_by_address(customers, address)
    elif option == 2:
        name = input("Enter the Name of the customer: ").strip()
        tempCustomers = search_customer_by_name(customers, name)
    else:
        print("Your option is invalid!")
        return

    if tempCustomers is None:
        print("No customer was found, try again")
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
    Search a customer by its address
    """
    result = list(filter(lambda customer: address.lower() in customer.address.lower(), customers))

    return result


def search_customer_by_name(customers: list[Customer], name: str):
    """
    Search a customer by its name
    """
    result = list(filter(lambda customer: name.lower() in customer.name.lower(), customers))

    return result


def update_customer(customers: list[Customer], customer: Customer, name=None, address=None):
    """
    Updates the proprerties of a customer
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
