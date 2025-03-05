"""
Decorator Pattern Implementation

This script demonstrates:
1. Function decorators
2. Closure functions
3. Decorator syntax using @
4. Function wrapping
5. Variable argument handling

Author: Shayan Mansornia
"""

# Example of closure function (commented out)
# def hello(name):
#     def hello_name():
#         print(f"Hello {name}")
#     return hello_name
# test = hello("Shayan")
# test()

def hello_decorator(func):
    """
    Decorator function that adds pre and post execution messages.
    
    Args:
        func: The function to be decorated
        
    Returns:
        function: Wrapped function with additional functionality
    """
    def wrapper(*args):
        print("hi this is before  the function")
        func(*args)
        print("this is after the function")

    return wrapper

@hello_decorator  # Decorator syntax
def hello(*args):
    """
    Function that prints a greeting with name and lastname.
    
    Args:
        *args: Variable arguments containing name and lastname
    """
    print(f"hello {name} {lastname}")

# Get user input and demonstrate decorated function
name = input("What is your name? ")
lastname = input("What is your last name? ")
hello(name, lastname)
