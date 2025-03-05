"""
Personal Greeting Generator

This script demonstrates:
1. Function definition with parameters
2. User input handling
3. String formatting with f-strings
4. Basic function calling

Author: Shayan Mansornia
"""

def my_name(name, city):
    """
    Generate a personalized greeting message.
    
    Args:
        name (str): The person's name
        city (str): The person's city
    """
    print(f"Hello {name} from {city}")

# Get user information
name = input("Enter your name: ")
city = input("Enter your city: ")

# Generate and display greeting
my_name(name, city)
