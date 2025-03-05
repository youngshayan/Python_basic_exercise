"""
List Comprehension and Filtering

This script demonstrates:
1. List filtering using loops
2. List comprehension syntax
3. String manipulation in list comprehension
4. List indexing
5. Multiple list operations

Author: Shayan Mansornia
"""

# Initialize list of names
names = ["amir", "Shayan", "Mahan", "sara", "pariya", "moli", "trou"]

# Filter names containing 'a' using traditional loop
new_list = []
for name in names:
    if "a" in name:
        new_list.append(name)
print(new_list)

# Demonstrate list comprehension for filtering
new_list = [name for name in names if "a" in name]
print(new_list)

# Demonstrate list comprehension with string manipulation
new_list = [name.upper() for name in names]
print(new_list)

# Demonstrate list indexing
print(names[0])