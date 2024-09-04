# dictionary in python
me = {
    "name": "Shayan",
    "lastname": "Mansornia",
    "age": 21,
    "friends": ['ali', 'reza', 'mohammed']
}
print(me['age'])

print(len(me))

print(me.get('name'))

print(me.keys())

print(me.values())

print(me.items())
# way to change a value
me["age"] = 22
print(me.values())
me.update({'age': 23})
print(me.get("age"))
# way to add a new item to dict
me["city"] = "tehran"
print(me.items())
me.update({"country": "Iran"})
print(me.values())

# way to remove item in dict
me.pop("country")
print(me)
print("-------------------------------------------------")
# way to copy a dict
me2 = me.copy()
print(me2)
me2.pop("friends")
print(me2)
print(me)
print("---------------------------------------------")
my_family = {
    "child1": {
        "name": "Shayan",
        "age": 21,
     },
    "child2": {
        "name": "mahan",
        "age": 16
     }
}
print(my_family["child1"])
my_family["child1"].update({"height": 178})
print(my_family)
