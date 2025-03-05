"""
Fibonacci Sequence Generator Module

This module implements a generator function that produces Fibonacci numbers up to a specified limit.
The implementation uses a generator pattern for memory efficiency when dealing with large sequences.

Author: Shayan Mansornia
"""

def fibonacci(limit):
    """
    Generate Fibonacci numbers up to the specified limit.
    
    Args:
        limit (int): The number of Fibonacci numbers to generate
        
    Yields:
        int: The next Fibonacci number in the sequence
        
    Example:
        >>> for num in fibonacci(5):
        ...     print(num)
        0
        1
        1
        2
        3
    """
    a = 0  # First number in the sequence
    b = 1  # Second number in the sequence
    fibs = []  # List to store generated numbers
    while len(fibs) < limit:
        fibs.append(a)
        yield a  # Yield the current number
        a = b
        b = a + b
    # return fibs  # Alternative return statement (commented out)

# Example usage
if __name__ == "__main__":
    x = fibonacci(100)
    for value in x:
        print(value)