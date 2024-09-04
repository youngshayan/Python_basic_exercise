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


class User:  # Parent class
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        print(f"Your name is {self.firstname} {self.lastname}")


class Student(User):  # Child class for students
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []

    def fullname(self):
        super().fullname()
        print("I'm a student")

    def choose_course(self, course_title):
        for course in courses:
            if course["Title"].lower() == course_title.lower():  # Case-insensitive matching
                self.courses.append(course)
                return True
        print(f"Course '{course_title}' not found.")
        return False

    def print_courses(self):
        if self.courses:
            print("Enrolled Courses:")
            for course in self.courses:
                print(course['Title'])
        else:
            print("This student has no enrolled courses.")


class Teacher(User):  # Child class for teachers
    def __init__(self, firstname, lastname, code):
        super().__init__(firstname, lastname)
        self.code = code

    def fullname(self):
        super().fullname()
        print("I'm a teacher")

    def add_course(self, course_title, teacher_name):
        existing_course = [course for course in courses if course["Title"].lower() == course_title.lower()]
        if existing_course:
            print(f"Course '{course_title}' already exists.")
            return False

        new_course = {"Title": course_title, "Teacher": teacher_name}
        courses.append(new_course)
        print(f"Course '{course_title}' added successfully.")
        return True


# Example usage
student1 = Student("Alice", "Smith", "alice.smith@example.com")
teacher1 = Teacher("Bob", "Jones", "TJ123")

# Student chooses a course
course_choice = input("Enter the course title you want to enroll in (or 'q' to quit): ")
while course_choice.lower() != 'q':
    if student1.choose_course(course_choice):
        print("Course added successfully!")
    course_choice = input("Enter another course title or 'q' to quit: ")

# Teacher adds a new course
new_course_title = input("Enter the title of the new course: ")
new_teacher_name = input("Enter the teacher's name for the new course: ")
if teacher1.add_course(new_course_title, new_teacher_name):
    print("Courses list updated.")

# Student prints enrolled courses
student1.print_courses()
