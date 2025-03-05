"""
User Authentication System

This script implements a simple user authentication system that:
1. Stores user credentials in a nested dictionary
2. Implements a login loop that continues until successful authentication
3. Validates user credentials against stored data
4. Demonstrates dictionary iteration and nested data structures

Author: Shayan Mansornia
"""

# Define user database with nested dictionaries
users = {
    "user1": {
        "name": "Shayan",
        "password": 12345
    },
    "user2": {
        "name": "mahan",
        "password": 12345
    }
}

# Main authentication loop
while True:
    # Get user credentials
    name = input("Enter your name: ")
    password = int(input("Enter your password: "))

    # Initialize flag for authentication status
    found = False
    
    # Check credentials against stored data
    for user in users.values():
        if user["name"] == name and user["password"] == password:
            found = True
            break

    # Handle authentication result
    if found:
        print("You've signed in successfully!")
        break
    else:
        print("WRONG USERNAME OR PASSWORD")
