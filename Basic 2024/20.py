"""
Inheritance Demonstration - Person and Student Classes

This script demonstrates:
1. Class inheritance
2. Parent and child class relationships
3. Method overriding
4. Super() function usage
5. Multiple inheritance levels

Author: Shayan Mansornia
"""

class Person:  # parent
    """
    Parent class representing a basic person with name attributes.
    
    Attributes:
        firstname (str): Person's first name
        lastname (str): Person's last name
    """
    
    def __init__(self, firstname, lastname):
        """
        Initialize a new person instance.
        
        Args:
            firstname (str): First name
            lastname (str): Last name
        """
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        """
        Display a greeting message with the person's full name.
        """
        print(f"Hello your name is {self.firstname}  {self.lastname}")

person1 = Person("Shayan", "Mansornia")
person1.print_name()


class Student(Person):  # child
    """
    Child class representing a student, inheriting from Person.
    
    Attributes:
        age (int): Student's age
    """
    
    def __init__(self, firstname, lastname, age):
        """
        Initialize a new student instance.
        
        Args:
            firstname (str): First name
            lastname (str): Last name
            age (int): Student's age
        """
        super().__init__(firstname, lastname)  # better way than the line 15
        self.age = age

    def print_age(self):
        """
        Display the student's age.
        """
        print(f"yor age is {self.age}")

student1 = Student("Reza", "Asqari", 21)
student1.print_name()
student1.print_age()