# to check the password validation
def pass_validation(password):
    if len(password) <= 8:
        print("Your password need to be at least 8 character! ")
    elif password.isnumeric():  # to check if all the string is number or not
        print("Your password must contain letter!")
    elif password.isalpha():  # to check if all the string is alphabet or not
        print("Your password must contain number! ")
    else:
        print(" congrats!!!!!!!!!\nYour password is valid!!!!!!")
        return True

while True:
    password = input("Enter your password: ")
    if pass_validation(password):
        break

