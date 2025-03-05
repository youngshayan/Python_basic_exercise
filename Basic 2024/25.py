"""
JSON Data Handling

This script demonstrates:
1. JSON string parsing
2. JSON object creation
3. Dictionary to JSON conversion
4. JSON data structure manipulation
5. Dictionary methods usage

Author: Shayan Mansornia
"""

# Import JSON library
import json

# Parse JSON string into Python object
x = '{ "name":"Shayan", "lastname":"mansornia", "IsMarried": true, "hello": false, "IsOld": null}'
y = json.loads(x)
print(y)
print(y.keys())

# Create Python dictionary
w = {
    "name": "Shayan",
    "lastname": "Mansornia",
    "age": 21,
    "friends": ['ali', 'reza', 'mohammed'],
    "you": True,
    "hello": None
}

# Convert dictionary to JSON string
xx = json.dumps(w)

# Demonstrate dictionary access and JSON conversion
print(w.get("age"))
print(xx)
