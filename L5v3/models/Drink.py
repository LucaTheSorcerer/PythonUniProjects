from models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_: int = None, name: str = None, portion_size: int = None, price: int = None,
                 alcohol: int = None):
        super().__init__(id_, name, portion_size, price)
        self.alcohol = alcohol

    def __eq__(self, other):
        return super().__eq__(other) and self.alcohol == other.alcohol

    def __str__(self):
        return super().__str__() + f", alcohol Content:{self.alcohol}"
