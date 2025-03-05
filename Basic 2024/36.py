"""
Variable Scope Demonstration

This script demonstrates:
1. Local variable scope
2. Global variable scope
3. Nested function scope
4. Global keyword usage
5. Variable shadowing

Author: Shayan Mansornia
"""

def test():
    """
    Outer function demonstrating variable scope.
    Contains a local variable x and a nested function.
    """
    x = 9  # local variable
    
    def test2():
        """
        Nested function demonstrating global variable modification.
        Uses the global keyword to modify the global variable x.
        """
        global x  # Declare x as global
        x = 18    # Modify global x
        print(x)  # Print modified global x
    
    test2()      # Call nested function
    print(x)     # Print local x (unchanged)

# Call the test function
test()

# Print the global x (modified by test2)
print(x)  # Prints 18