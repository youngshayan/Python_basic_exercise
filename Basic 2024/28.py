"""
Iterator Implementation and Usage

This script demonstrates:
1. Built-in iterator creation
2. Custom iterator class implementation
3. Iterator protocol methods
4. For loop iteration
5. Manual iteration using next()

Author: Shayan Mansornia
"""

# Demonstrate built-in iterator
name = "shayan" # iterable
my_iterator = iter(name) # iterator
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

class MyIter:
    """
    Custom iterator class that generates numbers from 1 to n.
    
    Attributes:
        number (int): Upper limit of iteration
    """
    
    def __init__(self, number):
        """
        Initialize the iterator.
        
        Args:
            number (int): Upper limit of iteration
        """
        self.number = number

    def __iter__(self):
        """
        Initialize iteration variables.
        
        Returns:
            self: The iterator object
        """
        self.a = 1
        return self

    def __next__(self):
        """
        Get the next number in sequence.
        
        Returns:
            int: Next number in sequence
            
        Raises:
            StopIteration: When sequence reaches upper limit
        """
        if self.a <= self.number:
            x = self.a # to start from 1 and not 2
            self.a += 1
            return x
        else:
            raise StopIteration

# Get user input and demonstrate iteration
number = int(input("Enter a number: "))
obj1 = MyIter(number)
for i in obj1:
    print(i)

# Example of manual iteration (commented out)
# my_iterator = iter(obj1)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

