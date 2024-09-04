#  to find the similar name in two lists
list1 = ['ali', 'reza', 'mehdi', 'shayan', 'ehsan', 'abtin', 'barsam', 'arian']
list2 = ['ali', 'mehdi', 'arian', 'asghar', 'sina', 'rajab', 'barsam']
newlist = []
for name in list1:
    for name2 in list2:
       if name == name2:
        newlist.append(name and name2)
print(newlist)
