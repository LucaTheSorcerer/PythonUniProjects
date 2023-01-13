from L5.modelle.Dish import Dish

class CookedDish(Dish):
    def __init__(self, id_ : int = None, name : str = None, portion_size : int = None, price : int = None, preparation_time : int = None):
        super().__init__(id_, name, portion_size, price)
        self.preparation_time = preparation_time

    def __eq__(self, other):
        return super().__eq__(other) and self.preparation_time == other.preparation_time

    def __str__(self):
        return super().__str__() + f", Preparation time = '{self.preparation_time}'"

    # def __hash__(self):
    #     encoded_string = self.__str__().encode()
    #     return hashlib.sha1(encoded_string).hexdigest()
    #
    # #Getter for preparation_time
    # @property
    # def preparation_time(self):
    #     return self.__preparation_time
    #
    # #Setter for preparation_time
    # @preparation_time.setter
    # def preparation_time(self, preparation_time):
    #     self.__preparation_time = preparation_time
