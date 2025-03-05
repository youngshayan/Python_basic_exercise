"""
Generator Function Demonstration

This script demonstrates:
1. Generator function definition
2. Yield statement usage
3. Generator iteration
4. Next() function usage
5. Generator state preservation

Author: Shayan Mansornia
"""

def generator():
    """
    A generator function that yields numbers 1, 2, and 3.
    
    Yields:
        int: Numbers 1, 2, and 3 in sequence
    """
    yield 1
    yield 2
    yield 3

# Create generator object
x = generator()

# Demonstrate iteration using for loop
for value in generator():
    print(value)

print("\n")

# Demonstrate manual iteration using next()
print(next(x))  # Prints 1
print(next(x))  # Prints 2
print(next(x))  # Prints 3
