# decorators in python
# def hello(name):
#     def hello_name():
#         print(f"Hello {name}")
#     return hello_name
# test = hello("Shayan")
# test()

def hello_decorator(func):
    def wrapper(*args, **kwargs):
        print("hi this is before  the function")
        func(*args, **kwargs)
        print("this is after the function")

    return wrapper

@hello_decorator # better syntax instead of line 20
def hello(*args, **kwargs):
    print(f"hello {name} {lastname}")
# hello = hello_decorator(hello)
name = input("What is your name? ")
lastname = input("What is your last name? ")
hello(name,lastname)
