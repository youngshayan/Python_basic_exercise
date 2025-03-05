"""
Character Counter

This script demonstrates:
1. String manipulation and cleaning
2. Character frequency counting
3. List-based duplicate prevention
4. String methods (lower, replace, count)

Author: Shayan Mansornia
"""

# Get user input and prepare for processing
value = input("Enter your sentence: ")
value = value.lower()  # Convert to lowercase for consistent counting
value = value.replace(" ", "")  # Remove all whitespace

# Initialize list to track processed characters
list1 = []

# Count frequency of each unique character
for x in value:
    if x not in list1:  # Only process each character once
        print(f"your sentence has {value.count(x)} : '{x}'")
        list1.append(x)  # Mark character as processed
