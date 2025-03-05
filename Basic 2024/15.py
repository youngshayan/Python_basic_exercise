"""
Number Parity Checker

This script demonstrates:
1. Function definition and calling
2. Number parity checking
3. User input handling
4. Program exit condition

Author: Shayan Mansornia
"""

def calc(number):
    """
    Check if a number is even or odd.
    
    Args:
        number (int): The number to check
    """
    if number % 2 == 0:
        print("Number is ---> even")
    else:
        print("Number is ---> odd")

# Main program loop
while True:
    print("type exit to close the program!!")
    number = int(input("\nEnter your number: "))
    calc(number)
    if number == "exit":
        break
