from L5.repository.DataRepo import DataRepo
from L5.repository.DataRepo import ResultCheck
from L5.repository.CustomerRepo import CustomerRepo
from L5.modelle.Customer import Customer
from L5.
from L5.ui.ui1 import *
class CustomerController:
    def __init__(self, customerRepo):
        self.__customerRepo = customerRepo


    def menu(self):
        option = menu("Manage customer", ["Show all customers", "Add a new customer", "Update customer",
                                          "Remove a customer", "Find a customer", "Return to the previous menu"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.menu()

        option = int(option)

        match option:
            case 1:
                self.__show_all_customers()
                self.menu()
            case 2:
                self.__add_customer()
                self.menu()
            case 3:
                self.__update_customer()
                self.menu()
            case 4:
                self.__remove_customer()
                self.menu()
            case 5:
                self.__search_customer()
                self.menu()
            case 6:
                pass
            case other:
                invalid_message_to_display()
                self.menu()
    def __show_all_customers(self):
        """
        Method for printing all customers
        :return:
        """
        header("Customers")
        customers = self.__customerRepo.load()
        for i in range(len(customers)):
            print(f"{i+1}. {customers[i]}")

    def __add_customer(self, customer):
        header("Add a new customer")
        name = input("Enter the customer's name: ")
        address = input("Enter the customer's address: ")

        customer = Customer(name, address)

        print("Add a new customer! ")
        result = self.__customerRepo.add(customer) #Implement add function
        if result == DataRepo.ResultCheck.SUCCES:
            print(f"The new customer {customer} has been successfully added")
        elif result == DataRepo.ResultCheck.ALREADY_EXISTS:
            print(f"The customer {customer} already exists in the database")
        self.__customerRepo.save([customer])

    def __update_customer(self):
        """
        This method is used to update the credentials
        of a customer
        :return:
        """
        header("Update a customer in the data base by its index")
        option = menu("Show customers", ["Show list", "Search customer"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.__update_customer()

        option = int(option)
        customers = []

        match option:
            case 1:
                customers = self.__customerRepo.get_all()
            case 2:
                option = menu("Search for customer by", ["Name", "Addresse"])
                if not option.isnumeric():
                    invalid_message_to_display()
                    self.menu()

                option = int(option)
                customer = Customer()

                match option:
                    case 1:
                        name = input("Enter the Name of the customer: ")
                        customer.name = name
                    case 2:
                        address = input("Enter the Address of the customer: ")
                        customer.adresse = address
                    case _:
                        invalid_message_to_display()
                        self.__update_customer()

                customers = self.__customerRepo.search(customer)
            case _:
                invalid_message_to_display()
                self.__update_customer()

        option = menu("Choose a customer", customers, "=")
        if not option.isnumeric():
            invalid_message_to_display()
            self.__update_customer()

        option = int(option)

        if option not in range(1, len(customers) + 1):
            invalid_message_to_display()
            self.__update_customer()

        cust = customers[option-1]
        print(f"The chosen customer is {cust}")

        print("Updated customer's information")

        name = input("Enter a new name for the cusomer: ")
        address = input("Enter a new address for the customer: ")

        updated_customer = Customer()

        if name != '':
            updated_customer.name = name
        if address != '':
            updated_customer.adresse = address

        result = self.__customerRepo.update(updated_customer) #Implement update function

        if result == ResultCheck.SUCCES:
            print(f"The customer {cust} has been updated to {updated_customer}")
        elif result == ResultCheck.NOT_FOUND:
            print(f"The customer {cust} has not been found!")

        print("=" * 10 + "Update Customer Information" + "=" * 10)
    def __remove_customer(self):
        """
        Method used to remove customer
        :return:
        """
        header("Remove customer by searching for index")
        option = menu("List of options", ["Show customers", "Search for customers"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.__remove_customer()

        option = int(option)
        customers = []

        match option:
            case 1:
                customers = self.__customerRepo.load()
            case 2:
                """
                Search customers in database
                """
                option = menu("Search for customer by", ["Name", "Address"])
                if not option.isnumeric():
                    invalid_message_to_display()
                    self.__remove_customer()
                option = int(option)
                customer = Customer()
                match option:
                    case 1:
                        name = input("Name of the customer: ")
                        customer.name = name
                    case 2:
                        addresse = input("Address of the customer: ")
                        customer.adresse = addresse
                    case other:
                        invalid_message_to_display()
                        self.__remove_customer()
                customers = self.__customerRepo.search(customer) #Implement search function in customer
            case _:
                invalid_message_to_display()
                self.__remove_customer()

        option = menu("Choose customer", customers)
        if not option.isnumeric():
            invalid_message_to_display()
            self.__remove_customer()

        option = int(option)

        if option not in range(1, len(customers)): #`Poate trebuie + 1:
            invalid_message_to_display()
            self.__remove_customer()

        c = customers[option-1]
        result = self.__customerRepo.remove(c) #Implement remove customer in customerRepo
        if result == DataRepo.ResultCheck.SUCCESS:
            print(f"The customer {c} was deleted")
        elif result == DataRepo.ResultCheck.NOT_FOUND:
            print(f"The customer {c} does not exist")

        print("Customer deleted by index")
        self.menu()




    def __search_customer(self):
        """
        Method used to search customers in file by name or address
        :return:
        """
        option = menu("search customer by", ["Name", "Address"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.__search_customer()

        option = int(option)
        customer = Customer()

        match option:
            case 1:
                """
                Search for customer by its Name
                """
                option = input("Name= ")
                customer = customer.name

            case 2:
                option = input("Address= ")
                customer = customer.adresse

            case other:
                invalid_message_to_display()
                self.__search_customer()

        header("Valid customers")
        customers = self.__customerRepo.search(customer) #implement search function

        for i in range(len(customers)):
            print(f"{i + 1}. {customers[i]}")

        print("Valid customers for the search")


    def get_customer_by_id(self, id):
        # return self.__customerRepo......(id)
        """
        Get the customer by id
        :param id:
        :return:
        """
        pass

    def get_customer_by_name(self, inputName):
        """
        Get the customer by name
        :param inputName:
        :return:
        """
        pass
        #return self.__customerRepo.get_by_name(inputName)

    def delete_customer(self, id):
        """
        Get the customer by name
        :param id:
        :return:
        """
        pass