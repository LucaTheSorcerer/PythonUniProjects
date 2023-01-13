from L5v2.models.Identifiable import Identifiable

class Customer(Identifiable):

    def __init__(self, id_ : int = None, name : str = "Ion", address : str = "Strada Eminescu numarul 8"):
        super().__init__(id_)
        self.name = name
        self.address = address

    def __eq__(self, other):
       return self.name == other.name and self.address == other.address

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}"