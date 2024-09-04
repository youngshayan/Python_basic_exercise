# users = {
#     "user1" : {
#     "name":"Shayan",
#     "password": 12345
#     },
#     "user2" : {
#         "name":"mahan",
#         "password": 12345

#     }
# }
# entered_username = input("Enter you username: ")
# entered_password = int(input("Enter you password: "))
# if entered_username in users and users['entered_username'] == entered_password:
#     print("You've signed in successfully!")
# else:
#     print("WRONG USERNAME OR PASSWORD")


# 
users = {
    "user1": {
        "name": "Shayan",
        "password": 12345
    },
    "user2": {
        "name": "mahan",
        "password": 12345
    }
}

while True:
    name = input("Enter your name: ")
    password = int(input("Enter your password: "))

    found = False
    for user in users.values():
        if user["name"] == name and user["password"] == password:
            found = True
            break

    if found:
        print("You've signed in successfully!")
        break
    else:
        print("WRONG USERNAME OR PASSWORD")
