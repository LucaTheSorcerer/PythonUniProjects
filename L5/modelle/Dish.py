from L5.modelle.Identifiable import Identifiable

class Dish(Identifiable):
    def __init__(self, id_, name : str, portion_size: int, price: float):

        if type(portion_size) != int or type(price) != float:
            raise AttributeError

        super().__init__(id_)
        self.__portion_size = portion_size
        self.__price = price
        self.__name = name

    def __eq__(self, other):
        return self.__name == other.__name and self.__price == other.__price \
            and self.__portion_size == other.__portion_size

    def __str__(self):
        return f"Name='{self.name}', Portion Size = '{self.portion_size}', Price = '{self.price}'"

    #Getter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):

        if type(self.__name) != str:
            raise AttributeError
        self.__name = name

    #Getter for portion_size
    @property
    def portion_size(self):
        return self.__portion_size

    #Setter for portion_size
    @portion_size.setter
    def portion_size(self, x: int):

        if type(self.__portion_size) != int:
            raise AttributeError

        self.__portion_size = x

    #Getter for price
    @property
    def price(self):
        return self.__price

    #Setter for price
    @price.setter
    def price(self, x: float):

        if type(self.__price) != float:
            raise AttributeError

        self.__price = x