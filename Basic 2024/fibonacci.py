def fibonacci(limit):
    a = 0
    b = 1
    fibs = []
    while len(fibs) < limit:
        fibs.append(a)
        yield a
        a = b
        b = a + b
    # return fibs

x = fibonacci(100)
for value in x:
    print(value)