import hashlib
from L5.modelle.Dish import Dish

class Drink(Dish):
    def __init__(self, id_ : int, name, portion_size : int, price : int, alcohol_content : int):
        super().__init__(id_, name, portion_size, price)

        if type(alcohol_content) != int:
            raise AttributeError

        self.__alcohol_content = alcohol_content

    def __eq__(self, other):
        return super().__eq__(other) and self.__alcohol_content == other.__alcohol_content

    def __str__(self):
        return super().__str__() + f", Alcohol Content = '{self.__alcohol_content}'"

    def __hash__(self):
        encoded_str = self.__str__().encode()
        return hashlib.sha1(encoded_str).hexdigest()

    #Getter for alcohol_content
    @property
    def alcohol_content(self):
        return self.__alcohol_content

    @alcohol_content.setter
    def alcohol_content(self, alcohol_content):
        self.__alcohol_content = alcohol_content