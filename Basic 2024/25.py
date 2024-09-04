import json
x = '{ "name":"Shayan", "lastname":"mansornia", "IsMarried": true, "hello": false, "IsOld": null}'
y = json.loads(x)
print(y)
print(y.keys())
w =  {
    "name": "Shayan",
    "lastname": "Mansornia",
    "age": 21,
    "friends": ['ali', 'reza', 'mohammed'],
    "you": True,
    "hello": None
}
xx = json.dumps(w)
print(w.get("age"))
print(xx)
