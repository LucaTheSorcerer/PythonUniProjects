from controller.CustomerController import add_new_customer, search_customer_by_address, search_customer_by_name, \
    update_customer, remove_customer
from models.Customer import Customer
from repository.CustomerRepo import CustomerRepo

"""
Here we test searching for a customer by name or address and changing the name of a customer
Thus here we test the functionalities of the CustomerRepo class
"""

customer1 = Customer(0, "Mihai", "Str. Ciocarliei nr. 19")
customer2 = Customer(1, "Gion", "Str. Luceafarului nr. 27")
customer3 = Customer(3, "hatz", "Str. Lucernei nr. 72")

repo = CustomerRepo("customers.txt")

repo.save([customer1, customer2])


def test_add_customer():
    customers = repo.load()
    customers = add_new_customer(customers, customer3)

    assert customer3 in customers

    repo.save(customers)

    customers = repo.load()

    assert customer3 in customers


def test_search_customer():
    customers = repo.load()
    c1 = search_customer_by_address(customers, "cioc")[0]

    assert c1 == customer1
    # print(c1)

    c2 = search_customer_by_name(customers, "hatz")[0]

    # print(c2)

    assert c2 == customer3


def test_update_customer():
    customers = repo.load()
    c1 = search_customer_by_address(customers, "cioc")[0]

    update_customer(customers, c1, "Mircea")

    c2 = search_customer_by_name(customers, "hatz")[0]

    update_customer(customers, c2, address="Strada Garii")

    print(customers[0])
    print(customers[1])
    print(customers[2])


def test_remove_customer():
    customers = repo.load()
    c1 = search_customer_by_address(customers, "cioc")[0]

    remove_customer(customers, c1)
    print(customers[0])
    print(customers[1])


test_add_customer()
test_search_customer()
test_update_customer()
test_remove_customer()
