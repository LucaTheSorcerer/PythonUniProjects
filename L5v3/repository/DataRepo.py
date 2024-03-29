class DataRepo:
    def __init__(self, file):
        self.file = file

    def add(self, obj):
        """
        This function should only be used for testing purposes
        :param obj: The objected to be added

        This function is used to append a new item to the specific database
        """
        obj_list = self.load()
        obj_list.append(obj)
        self.save(obj_list)

    def save(self, obj_list):
        """
        :param obj_list: A list of objects to be saved in the specific repository
        This function saves the list of objects to its specified repository
        """
        self.write_to_file(self.convert_to_string(obj_list))

    def load(self):
        """
        :return: The items from the specific repository as a list
        """
        return self.convert_from_string(self.read_file())

    def read_file(self):
        """
        :return: All the contents of the corresponding repository
        """
        with open(self.file, 'r') as f:
            content = f.read()
            f.close()
        return content

    def write_to_file(self, content):
        """
        :param content: The content to be written in the file
        This function writes the content in the file
        """
        with open(self.file, 'w') as f:
            f.write(content)
            f.close()

    def convert_to_string(self, obj_list):
        """
        This function is just defined here
        """
        pass

    def convert_from_string(self, string):
        """
        This function is just defined here
        """
        pass
