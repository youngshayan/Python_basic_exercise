"""
Class and Object Demonstration

This script demonstrates:
1. Class definition
2. Constructor method
3. Instance attributes
4. Object creation and access

Author: Shayan Mansornia
"""

class MyClass:
    """
    A class representing a person with basic attributes.
    
    Attributes:
        myname (str): Person's first name
        mylastname (str): Person's last name
        myage (int): Person's age
    """
    
    def __init__(self, name, lastname, age):
        """
        Initialize a new person instance.
        
        Args:
            name (str): First name
            lastname (str): Last name
            age (int): Age
        """
        self.myname = name
        self.mylastname = lastname
        self.myage = age

# Create instances of MyClass
person1 = MyClass("Shayan", "Mansornia", 22)
person2 = MyClass("Reza", "Mosavi", 25)

# Access instance attributes
print(person1.myage)
