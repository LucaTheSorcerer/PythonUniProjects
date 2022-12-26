class Identifiable:
    __id_counter = 0
    def __int__(self):
        self.__id = self.__class__.__id_counter
        self.__class__.__id_counter += 1
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id