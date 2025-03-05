"""
Function Arguments Demonstration

This script demonstrates:
1. Function with multiple argument types
2. *args for variable positional arguments
3. **kwargs for variable keyword arguments
4. String formatting with f-strings

Author: Shayan Mansornia
"""

def name(fname, lname, *args, **kwargs):
    """
    Display greeting and additional information.
    
    Args:
        fname (str): First name
        lname (str): Last name
        *args: Variable positional arguments
        **kwargs: Variable keyword arguments
    """
    print(f"Hello {fname}{lname}")
    print("args:", args)
    print("kwargs:", kwargs)

# Example usage with different argument types
name('shayan', 'mansornia', 'karaj', 'reza', age=23, height=170)
