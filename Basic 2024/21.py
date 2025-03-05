"""
Educational System - User Management with Inheritance

This script demonstrates:
1. Complex inheritance hierarchy
2. Method overriding with super()
3. List of dictionaries for course management
4. Multiple child classes (Student and Teacher)
5. Course enrollment functionality

Author: Shayan Mansornia
"""

# Define available courses
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


class User:
    """
    Parent class representing a basic user in the system.
    
    Attributes:
        firstname (str): User's first name
        lastname (str): User's last name
    """
    
    def __init__(self, firstname, lastname):
        """
        Initialize a new user instance.
        
        Args:
            firstname (str): First name
            lastname (str): Last name
        """
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        """
        Display the user's full name.
        """
        print(f"your name is {self.firstname} {self.lastname}")


class Student(User):
    """
    Child class representing a student, inheriting from User.
    
    Attributes:
        email (str): Student's email address
        courses (list): List of enrolled courses
    """
    
    def __init__(self, firstname, lastname, email):
        """
        Initialize a new student instance.
        
        Args:
            firstname (str): First name
            lastname (str): Last name
            email (str): Email address
        """
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []

    def fullname(self):
        """
        Override parent's fullname method to add student status.
        """
        super().fullname()
        print("I'm student")

    def print_courses(self):
        """
        Display all courses enrolled by the student.
        """
        if self.courses:
            for course in self.courses:
                print(course['Title'])
        else:
            print("This student have no course")


class Teacher(User):
    """
    Child class representing a teacher, inheriting from User.
    
    Attributes:
        code (int): Teacher's unique identification code
    """
    
    def __init__(self, firstname, lastname, code):
        """
        Initialize a new teacher instance.
        
        Args:
            firstname (str): First name
            lastname (str): Last name
            code (int): Teacher's ID code
        """
        super().__init__(firstname, lastname)
        self.code = code

    def fullname(self):
        """
        Override parent's fullname method to add teacher status.
        """
        super().fullname()
        print("I'm a teacher")

# Demonstrate course enrollment functionality
student1 = Student("Shayan", "Mansornia", "shayana@gamil.com")
student1.courses.append(courses[1])  # Enroll in PHP course
student1.print_courses()
print("__________________________")

student1.courses.append(courses[0])  # Enroll in Python course
student1.print_courses()
print("__________________________")

# Demonstrate new student with no courses
student2 = Student("Reza", "Ahamdi", "Reza@gamil.com")
student2.print_courses()