class Person:
    def __init__(self):
        self.a = 2 # public
        self._b = 13 # protected
        self.__age = 21 # private
    @property
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def del_age(self):
        del self.__age

    # age = property(get_age, set_age, del_age) # same as line 6

person1 = Person()


print(person1.get_age)

person1.set_age(33)
print(person1.get_age)

person1.age = 88 # To change the value easily
print(person1.age)

person1.age = 855
print(person1.age)


