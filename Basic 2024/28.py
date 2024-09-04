
name = "shayan" # iterable
my_iterator = iter(name) # iterator
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
class MyIter:
    def __init__(self, number):
        self.number = number
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= self.number:
            x = self.a # to start from 1 and not 2
            self.a += 1
            return x
        else:
            raise StopIteration
number = int(input("Enter a number: "))
obj1 = MyIter(number)
for i in obj1:
    print(i)
# my_iterator = iter(obj1)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

