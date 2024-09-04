class Car:
    cars_number = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False
        Car.cars_number += 1

    def start(self):
        if self.status == False:
            self.status = True
            print(f"Your car '{self.name}' is starting")
        else:
            print("Car is already started !!")

    def off(self):
        if self.status == True:
            self.status = False
            print(f"Your car '{self.name}' is turning off")
        else:
            print("Please start your car first !!!!!")

print(Car.cars_number)
print("_-------------------------_")
car1 = Car("benz", 1000)

car2 = Car("bmw", 2000)

car3 = Car("pride", 500)

car1.start()
car1.start()
car1.off()
car1.off()
print("_-------------------------_")
print(Car.cars_number)
