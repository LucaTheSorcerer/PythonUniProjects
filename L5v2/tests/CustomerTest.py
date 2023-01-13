from L5v2.models.Customer import Customer
from L5v2.repository.CustomerRepo import CustomerRepo

"""
Test for searching after a customer by its name or address and change its name
"""

customer1 = Customer(0, "Andrei", "Str. Blaga nr. 20")
customer2 = Customer(1, "Maria", "Str. Arghezi  nr. 35")

repo = CustomerRepo("customers.txt")

repo.save([customer1, customer2])

def search_customer_by_name_test():
    c1 = repo.search("and")[0]
    c2 = repo.search("ari")[0]

    assert c1 == customer1 and c2 == customer2


def search_customer_by_address():
    c1 = repo.search(address="aga")[0]
    c2 = repo.search(address="ghez")[0]

    assert c1 == customer1 and c2 == customer2

def update_customer_name():
    repo.update(customer1, "Luca")
    c1 = repo.load()[0]

    assert c1.name == "Luca"

def search_and_update_customer():
    c = repo.search("uca")[0]
    repo.update(c, "Tudor")
    c = repo.load()[0]

search_customer_by_name_test()
search_customer_by_address()
update_customer_name()
search_and_update_customer()