names = ["amir", "Shayan", "Mahan", "sara", "pariya", "moli", "trou"]
new_list = []
for name in names:
    if "a" in name:
        new_list.append(name)
print(new_list)

# list compression way
new_list = [name for name in names if "a" in name]
print(new_list)
new_list = [name.upper()for name in names ]
print(new_list)
print(names[0])