s = "Hello,bitches!!!"
print(str(s))
print(repr(s))

print(str((12.0 / 587.0)))
print(repr((12.0 / 587.0)))
print("\n")
class Teacher:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "shayan str"

    def __repr__(self):
        return "shayan repr"

t = Teacher("Shayan")
print(t)
print(repr(t))