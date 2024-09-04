courses = [
    {
        "Title": "Python",
        "Teacher": "Rezaee"
    },
    {
         "Title": "Php",
         "Teacher": "alavi"
    },
    {
        "Title": "HTML",
        "Teacher": "Shayeste"
    }
]


class User:  # parent
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        print(f"your name is {self.firstname} {self.lastname}")


class Student(User):  # child
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []

    # to update fullname method for student class
    def fullname(self):
        super().fullname()
        print("I'm student")

    def print_courses(self):
        if self.courses:
            for course in self.courses:
                print(course['Title'])
        else:
            print("This student have no course")


class Teacher(User):
    def __init__(self, firstname, lastname, code):
        super().__init__(firstname, lastname)
        self.code = code

    def fullname(self):
        super().fullname()
        print("I'm a teacher")

# student1 = Student("shayan", "mansornia", "Shayan@gmmail.com")
# teacher1 = Teacher("Ali", "dehyami", 212544522)
# student1.fullname()
# print("___________________")
# teacher1.fullname()
# ----------------------------------------------------------------

student1 = Student("Shayan", "Mansornia", "shayana@gamil.com")
student1.courses.append(courses[1])  # because it is a list and lists are indexed
# print(student1.courses)
student1.print_courses()
print("__________________________")
student1.courses.append(courses[0])
student1.print_courses()
print("__________________________")
student2 = Student("Reza", "Ahamdi", "Reza@gamil.com")
student2.print_courses()