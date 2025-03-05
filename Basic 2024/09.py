"""
List Intersection Finder

This script demonstrates:
1. Working with multiple lists
2. Nested loops for list comparison
3. Finding common elements between lists
4. List intersection operation

Author: Shayan Mansornia
"""

# Initialize two lists with names
list1 = ['ali', 'reza', 'mehdi', 'shayan', 'ehsan', 'abtin', 'barsam', 'arian']
list2 = ['ali', 'mehdi', 'arian', 'asghar', 'sina', 'rajab', 'barsam']

# Create empty list to store common names
newlist = []

# Find common names using nested loops
for name in list1:
    for name2 in list2:
        if name == name2:
            newlist.append(name)  # Add common name to result list

# Display the intersection of both lists
print(newlist)
