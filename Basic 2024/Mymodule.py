"""
User Management Module

This module provides basic functionality for user management including greeting messages
and user information handling. It includes both standalone functions and a User class
for object-oriented user management.

Author: Shayan Mansornia
"""

def hello(name):
    """
    Print a greeting message for the given name.
    
    Args:
        name (str): The name of the person to greet
        
    Example:
        >>> hello("John")
        hello John
    """
    print(f"hello {name}")


def sms(phone):
    """
    Display a message with the provided phone number.
    
    Args:
        phone (str): The phone number to display
        
    Example:
        >>> sms("123-456-7890")
        Your number is 123-456-7890
    """
    print(f"Your number is {phone}")


class User:
    """
    A class representing a user with basic information and functionality.
    
    Attributes:
        name (str): The name of the user
        
    Methods:
        printname(): Prints the user's name
    """
    
    def __init__(self, name):
        """
        Initialize a new User instance.
        
        Args:
            name (str): The name of the user
        """
        self.name = name

    def printname(self):
        """
        Print the user's name.
        
        Example:
            >>> user = User("Alice")
            >>> user.printname()
            Your name is Alice
        """
        print(f"Your name is {self.name}")