from enum import Enum

class ResultCheck(Enum):
    SUCCES = 1
    ALREADY_EXISTS = 2
    NOT_FOUND = 3

class DataRepo:
    def __init__(self, file):
        self.__file = file
        #self.load()
        self.entities : list = []

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file

    def save(self, objects : list):
        self.write_file(self.convert_to_string(objects))
        # for object in objects:
        #     if object not in self.entities:
        #         self.entities.append(object)
        #         self.write_file(self.convert_to_string(self.entities))

    def get_by_id(self, id):
        for entity in self.entities:
            if entity.id == id:
                return entity

    def load(self):
        string_content = self.read_file()
        return -1 if string_content == "" else string_content
        #self.entities = self.read_file() #content ---> string

    def read_file(self, content_read):
        with open(self.file, 'rb') as file:
            content_read = file.read()
            file.close()
        return content_read
       # return self.convert_from_string(lines)

    def write_file(self, string_content):
        with open(self.__file, 'wb') as file:
            file.write(string_content)
            file.close()

    def clear_database(self):
        file = open(self.__file, "wb")
        file.close()

    def __get_all_customers(self):
        pass


    def remove(self, object):
        object_list = self.load()
    def convert_to_string(self, objects):
        pass

    def convert_from_string(self, string_objects):
        pass


