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

    # def get_by_id(self, id):
    #     for entity in self.entities:
    #         if entity.id == id:
    #             return entity

    def load(self):
        string_content = self.read_file()
        return -1 if string_content == "" else self.convert_from_string(string_content)
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



    def add(self, obj):

        obj_list = self.load()
        obj.id = obj.__hash__()

        if obj_list == -1:
            self.save([obj])
            return ResultCheck.SUCCES

        if obj not in obj_list:
            obj_list.append(obj)
            self.save(obj_list)
            return ResultCheck.SUCCES
        else:
            return ResultCheck.ALREADY_EXISTS


    def add_list(self, objects):
        obj_list = self.load()
        result = ResultCheck.SUCCES

        if obj_list == -1:
            for obj in obj_list:
                obj.id = obj.__hash__()
            self.save(objects)
            return result

        for obj in obj_list:
            if obj not in obj_list:
                obj.id = obj.__hash__()
                obj_list.append(obj)
            else:
                result = ResultCheck.ALREADY_EXISTS

        self.save(obj_list)
        return result


    def remove(self, object):
        object_list = self.load()

        if object_list == -1:
            return ResultCheck.NOT_FOUND

        new_list = list(filter(lambda o: o != object, object_list))


        if len(new_list) != len(object_list):
            self.save(new_list)
            return ResultCheck.SUCCES
        else:
            return ResultCheck.NOT_FOUND

    def update(self, object, updated_object):
        assert type(object) == type(updated_object)
        object_list = self.load()
        listt = list(filter(lambda o : o == object, object_list))
        if len(listt) > 0:
            attribute_list = list(filter(lambda a: '_' not in a and a != 'id', dir(updated_object)))
            for attribute in attribute_list:
                attribute_value = getattr(updated_object, attribute)
                if attribute_value is not None:
                    setattr(listt[0], attribute, attribute_value)

            self.save(object_list)
            return ResultCheck.SUCCES
        return ResultCheck.NOT_FOUND


    def search(self, object):
        object_list = self.load()

        for attribute in dir(object):
            if getattr(object, attribute) is not None:
                if type(attribute) is str:
                    filtered = list(filter(lambda o : getattr(object, attribute).lower() in getattr(o, attribute).lower(), object_list))
                    return filtered
                else:
                    filtered = list(filter(lambda o : getattr(object, attribute) == getattr(o, attribute), object_list))

        return []

    def find_by_id(self, id_):
        object_list = self.load()

        for object in object_list:
            if object.id == id_:
                return object

        return ResultCheck.NOT_FOUND


    def find_by_ids(self, ids):
        res = []
        for id_ in ids:
            object = self.find_by_id(id_)
            if object is not ResultCheck.NOT_FOUND:
                res.append(object)

        return res


    def get_all(self):
        object_list = self.load()
        return object_list if object_list != 1 else []

    def clear(self):
        self.clear_database()
    def convert_to_string(self, objects):
        pass

    def convert_from_string(self, string_objects):
        pass


