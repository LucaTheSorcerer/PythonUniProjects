from L5v2.models.Dish import Dish

class CookedDish(Dish):
    def __init__(self, id_ : int = None, name : str = None, portion_size: int = None, price: int = None,
                 preparation_time: int = None):
        super().__init__(id_, name, portion_size, price)
        self.preparation_time = preparation_time

    def __eq__(self, other):
        return super().__eq__(other) and self.preparation_time == other.preparation_time

    def __str__(self):
        return super().__str__() + f", Preparation Time: {self.preparation_time}"