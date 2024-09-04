def generator():
    yield 1
    yield 2
    yield 3
x = generator()

for value in generator():
    print(value)

print("\n")

print(next(x))
print(next(x))
print(next(x))
