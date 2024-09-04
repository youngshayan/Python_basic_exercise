from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass
 
    def legs(self):
        pass

class Dog(Animal):
    def move(self):
        print('Dog is moving.')
    @property
    def legs(self):
        return 4


class Cat(Animal):
    def move(self):
        print('Cat is moving.')
    @property
    def legs(self):
        return 3

d1 = Dog()
c1 = Cat()
d1.move()
c1.move()
print(d1.legs)
print(c1.legs)