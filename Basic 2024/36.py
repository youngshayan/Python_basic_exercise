
def test():
    x = 9  # local
    def test2():
        global x # global
        x = 18
        print(x)
    test2()
    print(x) # prints local x
test()
print(x) # prints global x