"""
Multiple Decorator Chain Demonstration

This script demonstrates:
1. Multiple decorator chaining
2. Decorator order of execution
3. Function return value manipulation
4. Nested decorator functions
5. Mathematical operation decorators

Author: Shayan Mansornia
"""

def decorator1(func):
    """
    Decorator that squares the return value of a function.
    
    Args:
        func: The function to be decorated
        
    Returns:
        function: Wrapped function that squares the result
    """
    def wrapper():
        x = func()
        return x * x
    return wrapper


def decorator2(func):
    """
    Decorator that doubles the return value of a function.
    
    Args:
        func: The function to be decorated
        
    Returns:
        function: Wrapped function that doubles the result
    """
    def wrapper():
        x = func()
        return 2 * x
    return wrapper


@decorator1  # Applied last (outermost)
@decorator2  # Applied first (innermost)
def test():
    """
    Test function that returns a fixed value.
    
    Returns:
        int: The value 5
    """
    return 5

# Demonstrate decorator chain execution
print(test())  # Result: (2 * 5)² = 100
