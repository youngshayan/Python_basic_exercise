"""
Car Class with State Management

This script demonstrates:
1. Class with class variables
2. Instance state management
3. Method implementation with conditions
4. Object creation and method calling

Author: Shayan Mansornia
"""

class Car:
    """
    A class representing a car with state management functionality.
    
    Class Variables:
        cars_number (int): Total number of car instances created
        
    Instance Attributes:
        name (str): Car's name
        price (float): Car's price
        status (bool): Car's current state (running/stopped)
    """
    
    cars_number = 0  # Class variable to track total cars

    def __init__(self, name, price):
        """
        Initialize a new car instance.
        
        Args:
            name (str): Car's name
            price (float): Car's price
        """
        self.name = name
        self.price = price
        self.status = False
        Car.cars_number += 1  # Increment total cars counter

    def start(self):
        """
        Start the car if it's not already running.
        """
        if self.status == False:
            self.status = True
            print(f"Your car '{self.name}' is starting")
        else:
            print("Car is already started !!")

    def off(self):
        """
        Turn off the car if it's currently running.
        """
        if self.status == True:
            self.status = False
            print(f"Your car '{self.name}' is turning off")
        else:
            print("Please start your car first !!!!!")

# Display initial number of cars
print(Car.cars_number)
print("_-------------------------_")

# Create car instances
car1 = Car("benz", 1000)
car2 = Car("bmw", 2000)
car3 = Car("pride", 500)

# Demonstrate car operations
car1.start()
car1.start()  # Try to start already running car
car2.start()
car2.start()  # Try to start already running car

car1.off()
car1.off()  # Try to turn off already stopped car
car2.off()

print("_-------------------------_")
# Display final number of cars
print(Car.cars_number)
