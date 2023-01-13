from models.Customer import Customer


def search_customer_prints():
    print("Enter the name or the address of the customer you are searching for")
    print("You can search either by address or by name, not both")
    print("Enter 1 to search by address")
    print("Enter 2 to search by name")


def add_new_customer_input():
    """
    :return: The input that the add_new_customer function needs
    This is a sister function for the add_new_customer function
    """
    print("A customer has the following attributes: a name and an address")
    name = input("Name: ").strip()
    address = input("Address: ").strip()

    return Customer(name=name, address=address)
