lists = ['ali', 'shayan', 'mohammad', 'reza']
print("\n\ntype ------->", type(lists))
print(lists)
print(lists[0:2])  # only show from index 0 (included) and 2 (not included)

# the way you can change an item in a list
lists[1] = "Shayannn"
print(lists)

lists[0:2] = "ali2", "shayan2"
print(lists)

# to only replace ali2 with two new item
lists[0:1] = "sadegh", "hossein"
print(lists)

# the way you can insert a new value in index
lists.insert(1, "abtin")
print(lists)

list_lenght = len(lists)
print(f"length of the list is now: {list_lenght}\n")

# add the new value to the end of list
lists.append('iran')
print(lists)

# to merge two or more list together
new_list = [1, 2, 2, 3, 4, 5]
lists.extend(new_list)
print(lists)

# to remove an item from list
lists.remove('hossein')
print(lists)
lists.pop(1)
print(lists)

# to sort a list
list1 = ['wli', 'reza', 'bahram', 'dash', 'ali', 'cara']
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
