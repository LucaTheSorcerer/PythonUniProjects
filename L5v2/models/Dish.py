from L5v2.models.Identifiable import Identifiable

class Dish(Identifiable):
    def __init__(self, id_ = None, name = None, portion_size = None, price = None):
        super().__init__(id_)
        self.name = name
        self.portion_size = portion_size
        self.price = price


    def __eq__(self, other):
        return self.name == other.name and self.portion_size == other.portion_size and self.price == other.price

    def __str__(self):
        return f"Name: '{self.name}', Size: '{self.portion_size}', Price: '{self.price}'"