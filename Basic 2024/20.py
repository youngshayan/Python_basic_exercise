class Person:  # parent
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(f"Hello your name is {self.firstname}  {self.lastname}")

person1 = Person("Shayan", "Mansornia")
person1.print_name()


class Student(Person):  # child
    def __init__(self, firstname, lastname, age):
        # Person.__init__(self, firstname, lastname)
        super().__init__(firstname, lastname)  # better way than the line 15
        self.age = age

    def print_age(self):
        print(f"yor age is {self.age}")

student1 = Student("Reza", "Asqari", 21)
student1.print_name()
student1.print_age()