"""
Property Decorator and Access Modifiers

This script demonstrates:
1. Property decorator usage
2. Access modifiers (public, protected, private)
3. Getter and setter methods
4. Property deletion
5. Encapsulation principles

Author: Shayan Mansornia
"""

class Person:
    """
    A class demonstrating property decorator and access modifiers.
    
    Attributes:
        a (int): Public attribute
        _b (int): Protected attribute (single underscore)
        __age (int): Private attribute (double underscore)
    """
    
    def __init__(self):
        """
        Initialize person attributes with different access levels.
        """
        self.a = 2      # public
        self._b = 13    # protected
        self.__age = 21 # private

    @property
    def get_age(self):
        """
        Getter method for private age attribute.
        
        Returns:
            int: The person's age
        """
        return self.__age

    def set_age(self, age):
        """
        Setter method for private age attribute.
        
        Args:
            age (int): New age value
        """
        self.__age = age

    def del_age(self):
        """
        Deletion method for private age attribute.
        """
        del self.__age

    # age = property(get_age, set_age, del_age)  # Alternative property definition


# Demonstrate property usage
person1 = Person()

# Access age through property
print(person1.get_age)

# Modify age using setter
person1.set_age(33)
print(person1.get_age)

# Modify age using property assignment
person1.age = 88
print(person1.age)

# Further age modification
person1.age = 855
print(person1.age)


