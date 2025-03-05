"""
Name Filter - First Letter Matcher

This script demonstrates:
1. List iteration using for loops
2. String indexing to check first character
3. List filtering based on character matching
4. Basic list operations and string manipulation

Author: Shayan Mansornia
"""

# Initialize list of names
names = ['ali', 'reza', 'mehdi', 'shayan', 'ehsan', 'abtin', 'barsam', 'arian']

# Create empty list to store matching names
lists = []

# Iterate through names and filter those starting with 'a'
for name in names:
    if name[0] == "a":
        lists.append(name)

# Display filtered results
print(lists)
