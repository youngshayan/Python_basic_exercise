"""
Number Game - Mathematical Operations

This script implements a simple mathematical game that:
1. Takes a number between 1 and 9 as input
2. Performs a series of mathematical operations
3. Always results in the number 8 if the input is valid
4. Demonstrates input validation and mathematical operations

Author: Shayan Mansornia
"""

# Get user input and convert to integer
number1 = int(input("\nEnter a number between 1 and 9 ----> "))

# Validate input is between 1 and 9
if 1 <= number1 <= 9:
    # Perform series of mathematical operations
    number = number1 * 2      # Multiply by 2
    number += 8              # Add 8
    number += number1        # Add original number
    number -= 2              # Subtract 2
    number /= 3              # Divide by 3
    number -= number1        # Subtract original number
    number *= 4              # Multiply by 4
    number = int(number)     # Convert to integer
    
    # Display the result (should always be 8)
    print(f'\nYour final answer must be 8 and it is ----> {number} \n')
else:
    # Handle invalid input
    print("The number you've entered isn't between 1 and 9.")
# small game
