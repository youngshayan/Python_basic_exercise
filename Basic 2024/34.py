"""
String Representation Methods

This script demonstrates:
1. str() and repr() functions
2. __str__ method implementation
3. __repr__ method implementation
4. String formatting differences
5. Object string representation

Author: Shayan Mansornia
"""

# Demonstrate str() and repr() with strings
s = "Hello,bitches!!!"
print(str(s))    # Human-readable string representation
print(repr(s))   # Detailed string representation with quotes

# Demonstrate str() and repr() with numbers
print(str((12.0 / 587.0)))    # Human-readable number representation
print(repr((12.0 / 587.0)))   # Detailed number representation
print("\n")

class Teacher:
    """
    A class demonstrating string representation methods.
    
    Attributes:
        name (str): Teacher's name
    """
    
    def __init__(self, name):
        """
        Initialize a new teacher instance.
        
        Args:
            name (str): Teacher's name
        """
        self.name = name

    def __str__(self):
        """
        Return a human-readable string representation of the object.
        
        Returns:
            str: Human-readable string
        """
        return "shayan str"

    def __repr__(self):
        """
        Return a detailed string representation of the object.
        
        Returns:
            str: Detailed string representation
        """
        return "shayan repr"

# Create instance and demonstrate string representations
t = Teacher("Shayan")
print(t)         # Uses __str__
print(repr(t))   # Uses __repr__