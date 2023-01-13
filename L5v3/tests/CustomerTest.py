from models.Customer import Customer
from repository.CustomerRepo import CustomerRepo

"""
Here we test searching for a customer by name or address and changing the name of a customer
Thus here we test the functionalities of the CustomerRepo class
"""

customer1 = Customer(0, "Mihai", "Str. Ciocarliei nr. 19")
customer2 = Customer(1, "Gion", "Str. Luceafarului nr. 27")

repo = CustomerRepo("customers.txt")

repo.save([customer1, customer2])


def search_customer_by_name_test():
    # print(repo.search("mih")[0])
    # print(repo.search("ion")[0])

    c1 = repo.search("mih")[0]
    c2 = repo.search("ion")[0]

    assert c1 == customer1 and c2 == customer2


def search_customer_by_address():
    c1 = repo.search(address="cioc")[0]
    c2 = repo.search(address="farului")[0]

    # print(c1)
    # print(c2)

    assert c1 == customer1 and c2 == customer2


def update_customer_name():
    repo.update(customer1, "Andrei")
    c1 = repo.load()[0]

    # print(c1)

    assert c1.name == "Andrei"


def search_and_update_customer():
    c = repo.search("and")[0]
    repo.update(c, "Mircea")
    c = repo.load()[0]
    # print(c)


search_customer_by_name_test()
search_customer_by_address()
update_customer_name()
search_and_update_customer()
