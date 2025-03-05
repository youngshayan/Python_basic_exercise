"""
String Length Calculator

This script demonstrates basic string manipulation by:
1. Taking user input for a sentence
2. Calculating the length of the input string
3. Displaying the result using f-string formatting

Author: Shayan Mansornia
"""

# Get user input for the sentence
text = input("Enter your sentence:")

# Calculate the length of the input string
char_length = len(text)

# Display the result using f-string formatting
print(f"The length of your string is :{char_length}")

# Note: This is a simple implementation of string length calculation
# The len() function counts all characters including spaces and special characters
