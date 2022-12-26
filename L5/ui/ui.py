

from L5.modelle.Customer import Customer


class Console():
    def __init__(self, customerController):
        self.__customerController = customerController

    def run(self):
        # while True:
        #     self.print_menu()
        #     option = int(input("Enter a valid input! "))
        #     if option == 1:
        #         self.print_customers_menu()
        #         self.manage_customers()
        #     elif option == 2:
        #         pass
        #     elif option == 3:
        #         pass
        #     else:
        #         exit()


    def print_menu(self):
        print("**************************")
        print("1. Manage Customers")
        print("2. Manage Orders")
        print("3. Manage Menu")
        print("0. Exit")

    def print_customers_menu(self):
        print("====== Manage Customers ======")
        print("1. Add customer")
        print("2. View Customer")
        print("3. Update Customers")
        print("4. Remove Customers")


    # def manage_customers(self):
    #     manage_customer_input = int(input("Enter an option to manage customers"))
    #     if(manage_customer_input == 1):
    #         name = input("Insert customer's name")
    #         address = input("Insert customer's address")
    #         self.create_customer(name, address)
    #     elif manage_customer_input == 2:
    #         # get id of the user to be viewd
    #         #print(self.get_customer(id))
    #         pass


    # def create_customer(self, name, address):
    #     # validation takes place here --> name is string? address is string?? .....
    #     customer = Customer(name, address)
    #     self.__customerController.add_customer(customer)



    #WELCOME TO APP
    # 1. Manage Customers
    # 2. Manage Orders
    # 3. Manage Menu
    # 0. Exit






