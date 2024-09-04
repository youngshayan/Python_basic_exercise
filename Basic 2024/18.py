class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def fullname(self):
        print(f"hello {self.name} {self.lastname} how are you?")

p1 = Person("Shayan", "Mansornia")
p2 = Person("Mahan", "manrrroni")

p1.fullname()
# way to change item value
p1.name = "Reza"
p1.lastname = "Rezaee"
p1.fullname()
