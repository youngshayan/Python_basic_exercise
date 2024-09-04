#  for loop exercise to find name which starts with a
names = ['ali', 'reza', 'mehdi', 'shayan', 'ehsan', 'abtin', 'barsam', 'arian']
lists = []
for name in names:
    if name[0] == "a":
        lists.append(name)
print(lists)
