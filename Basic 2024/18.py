"""
Person Class with Method Demonstration

This script demonstrates:
1. Class with instance methods
2. Instance attribute modification
3. String formatting in methods
4. Object creation and method calling

Author: Shayan Mansornia
"""

class Person:
    """
    A class representing a person with name attributes and greeting functionality.
    
    Attributes:
        name (str): Person's first name
        lastname (str): Person's last name
    """
    
    def __init__(self, name, lastname):
        """
        Initialize a new person instance.
        
        Args:
            name (str): First name
            lastname (str): Last name
        """
        self.name = name
        self.lastname = lastname

    def fullname(self):
        """
        Display a greeting message using the person's full name.
        """
        print(f"hello {self.name} {self.lastname} how are you?")

# Create person instances
p1 = Person("Shayan", "Mansornia")
p2 = Person("Mahan", "manrrroni")

# Demonstrate method calling
p1.fullname()

# Demonstrate attribute modification
p1.name = "Reza"
p1.lastname = "Rezaee"
p1.fullname()
