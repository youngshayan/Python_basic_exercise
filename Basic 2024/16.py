"""
Gregorian to Hijri Year Converter

This script demonstrates:
1. Date conversion logic
2. Function with multiple parameters
3. Conditional statements
4. User input handling

Author: Shayan Mansornia
"""

def converter(year, month, day):
    """
    Convert Gregorian date to Hijri year.
    Note: This is a simplified conversion that adds 621 or 622 years
    depending on the date's position relative to Nowruz (Persian New Year).
    
    Args:
        year (int): Gregorian year
        month (int): Month (1-12)
        day (int): Day of month
    """
    if day >= 11 and 10 <= month <= 12:
        year += 622
        print(f"Your birthday is in {year}")
    else:
        year += 621
        print(f"Your birthday is in {year}")

# Get user's birth date
day = int(input("Enter the day of your birthday: "))
month = int(input("Enter the month of your birthday: "))
year = int(input("Enter the year of your birthday: "))

# Convert and display result
converter(year, month, day)


