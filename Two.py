class UnacceptedValue(Exception):
    pass


# a)
class DecryptedText:
    def __init__(self, characters: list[str]):
        self.characters = characters

    def encrypt(self):
        ascii_code = []
        for c in self.characters:
            if not c.islower():  # method for verifying if the character is a lower case letter
                raise UnacceptedValue
            else:
                ascii_code.append(ord(c))  # ord - converting to ascii value
        return ascii_code


d = DecryptedText(['a', 'b', 'c'])
print(d.characters)
print(d.encrypt())


# b)
class ActualDecryptedText(DecryptedText):
    def __init__(self, characters):
        super().__init__(characters)
        self.numbers = None

    def encrypt(self):
        try:
            self.numbers = super().encrypt()
        except UnacceptedValue:
            self.numbers = []

    def __add__(self, other: int):
        new_instance = ActualDecryptedText(self.characters)
        new_instance.encrypt()

        for i in range(len(new_instance.numbers)):
            new_instance.numbers[i] += other

        return new_instance


def main():
    c1 = ActualDecryptedText(['a', 'b', 'c'])
    c1.encrypt()
    c2 = ActualDecryptedText(['d', 'e', 'f'])
    c2.encrypt()
    c3 = c1 + 3
    print(c3.numbers)


main()
