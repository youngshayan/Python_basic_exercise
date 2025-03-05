"""
Exception Handling Demonstration

This script demonstrates:
1. Try-except block usage
2. Exception raising
3. Else clause in try-except
4. Finally block execution
5. Custom error messages

Author: Shayan Mansornia
"""

try:
    # Attempt to print undefined variable 'x'
    print(x)
except:
    # Raise a custom KeyError with message
    raise KeyError("We have an error")
else:
    # Execute if no exception occurs
    print("I''m from else")
finally:
    # Always execute, regardless of exception
    print("I'm from finally")