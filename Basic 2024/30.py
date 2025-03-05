"""
Function Execution Time Calculator

This script demonstrates:
1. Time measurement decorator
2. Function execution timing
3. Decorator with multiple argument types
4. Sleep function usage
5. Time module functionality

Author: Shayan Mansornia
"""

import time


def timecalc(func):
    """
    Decorator that measures and prints the execution time of a function.
    
    Args:
        func: The function to be timed
        
    Returns:
        function: Wrapped function with timing functionality
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"total time is: {end - start}")
    return wrapper


@timecalc
def hello(*args, **kwargs):
    """
    Function that prints a greeting after a delay.
    
    Args:
        *args: Variable positional arguments
        **kwargs: Variable keyword arguments
    """
    time.sleep(2)  # Simulate some processing time
    print(f"Hello {name} !")

# Get user input and demonstrate timed function
name = input("What is your name? ")
hello(name)
