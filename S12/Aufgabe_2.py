import re
def validate1(s):
    if len(s) != 8:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s[2] == '-':
        return False
    if not s[3].isnumeric() or not s[4].isnumeric():
        return False
    if not s[5] == '-':
        return False
    if not s[6].isalpha() or not s[7].isalpha() or not s[8].isalpha():
        return False
    return True




def validate(s):
    pattern = re.compile(r'^[A-Z]{2}-\d{2}-[A-Z]{3}$')
    return True if pattern.match(s) else False


def main():
    print(validate1("JA-12-BDG"))
    print(validate("JA-12-BDG"))

main()
