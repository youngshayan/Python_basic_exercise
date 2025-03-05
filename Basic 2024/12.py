"""
Password Validator

This script demonstrates:
1. Password validation rules implementation
2. String methods (isnumeric, isalpha)
3. Function with return values
4. Input validation loop

Author: Shayan Mansornia
"""

def pass_validation(password):
    """
    Validate password according to security rules:
    - Must be at least 8 characters long
    - Must contain both letters and numbers
    
    Args:
        password (str): The password to validate
        
    Returns:
        bool: True if password is valid, False otherwise
    """
    if len(password) <= 8:
        print("Your password need to be at least 8 character! ")
    elif password.isnumeric():  # Check if password contains only numbers
        print("Your password must contain letter!")
    elif password.isalpha():  # Check if password contains only letters
        print("Your password must contain number! ")
    else:
        print(" congrats!!!!!!!!!\nYour password is valid!!!!!!")
        return True

# Main password validation loop
while True:
    password = input("Enter your password: ")
    if pass_validation(password):
        break

