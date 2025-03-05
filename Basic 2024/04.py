"""
List Manipulation and Operations

This script demonstrates various list operations in Python including:
1. List creation and type checking
2. List slicing and indexing
3. List modification methods (insert, append, extend)
4. List removal methods (remove, pop)
5. List sorting and reverse sorting

Author: Shayan Mansornia
"""

# Initialize a list with names
lists = ['ali', 'shayan', 'mohammad', 'reza']

# Demonstrate type checking
print("\n\ntype ------->", type(lists))
print(lists)

# Demonstrate list slicing
print(lists[0:2])  # only show from index 0 (included) and 2 (not included)

# Demonstrate single item modification
lists[1] = "Shayannn"
print(lists)

# Demonstrate multiple item replacement
lists[0:2] = "ali2", "shayan2"
print(lists)

# Demonstrate replacing one item with multiple items
lists[0:1] = "sadegh", "hossein"
print(lists)

# Demonstrate insert method
lists.insert(1, "abtin")
print(lists)

# Get and display list length
list_lenght = len(lists)
print(f"length of the list is now: {list_lenght}\n")

# Demonstrate append method
lists.append('iran')
print(lists)

# Demonstrate extend method for merging lists
new_list = [1, 2, 2, 3, 4, 5]
lists.extend(new_list)
print(lists)

# Demonstrate remove and pop methods
lists.remove('hossein')
print(lists)
lists.pop(1)
print(lists)

# Demonstrate list sorting
list1 = ['wli', 'reza', 'bahram', 'dash', 'ali', 'cara']
print(list1)

# Sort in ascending order
list1.sort()
print(list1)

# Sort in descending order
list1.sort(reverse=True)
print(list1)
