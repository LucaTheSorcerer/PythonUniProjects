from L5v2.models.Dish import Dish

class Drink(Dish):
    def __init__(self, id_: int = None, name: str = None, portion_size: int = None, price: int = None,
                 alcohol_content: int = None):
        super().__init__(id_, name, portion_size, price)
        self.alcohol_content = alcohol_content

    def __eq__(self, other):
        return super().__eq__(other) and self.alcohol_content == other.alcohol_content

    def __str__(self):
        return super().__str__() + f", Alcohol Content: {self.alcohol_content}"