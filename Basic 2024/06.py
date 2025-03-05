"""
Odd-Even Number Checker

This script implements a simple program that:
1. Takes user input for numbers
2. Checks if each number is odd or even
3. Uses a while loop to process multiple inputs
4. Demonstrates basic conditional logic

Author: Shayan Mansornia
"""

# Initialize counter for loop
i = 1

# Loop to process 10 numbers
while i <= 10:
    # Get user input and convert to integer
    num = int(input("Enter a number to see if it's odd or even: "))
    i += 1
    
    # Check if number is even or odd using modulo operator
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
