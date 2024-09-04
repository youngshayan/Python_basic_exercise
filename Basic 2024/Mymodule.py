def hello(name):
    print(f"hello {name}")


def sms(phone):
    print(f"Your number is {phone}")


class User:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(f"Your name is {self.name}")