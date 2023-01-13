from L5v2.models.Customer import Customer

def search_customer_prints():
    print("Enter the name or the address of the customer you are searching for")
    print("You can either search by its name or by its address")
    print("Enter 1 to search by address")
    print("Enter 2 to search by name")

def add_new_customer_input():
    """
    :return: input for the add_new_customer function
    """
    print("A customer has the following attributes: name and address")
    name = input("Name: ").strip()
    address = input("Address: ").strip()

    return Customer(name=name, address=address)