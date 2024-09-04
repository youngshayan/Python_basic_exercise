import time


def timecalc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"total time is: {end - start}")
    return wrapper


@timecalc
def hello(*args, **kwargs):
    time.sleep(2)
    print(f"Hello {name} !")

name = input("What is your name? ")
hello(name)
