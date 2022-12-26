from L5.modelle.Identifiable import Identifiable

class Customer(Identifiable):
    def __init__(self, name: str, adresse: str):
        if type(name) != str or type(adresse) != str:
            raise AttributeError
        super().__int__()
        self.name = name
        self.adresse = adresse



        @property
        def adresse(self):
            return self.__adresse

        @adresse.setter
        def adresse(self, x:str):
            if type(self.__adresse) != str:
                raise AttributeError

            self.__adresse = x

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, x:str):
            if type(self.__name) != float:
                raise AttributeError

            self.__name = x


