def decorator1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decorator2(func):
    def wrapper():
        x = func()
        return 2 * x
    return wrapper

@decorator1
@decorator2
def test():
    return 5

print(test())
