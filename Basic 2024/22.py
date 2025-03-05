"""
Advanced Educational System - Course Management

This script demonstrates:
1. Complex inheritance hierarchy
2. Course management system
3. Interactive course enrollment
4. Course addition functionality
5. Case-insensitive string matching
6. List comprehension usage

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
        print(f"Your name is {self.firstname} {self.lastname}")


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
        print("I'm a student")

    def choose_course(self, course_title):
        """
        Enroll the student in a course by title.
        
        Args:
            course_title (str): Title of the course to enroll in
            
        Returns:
            bool: True if enrollment successful, False otherwise
        """
        for course in courses:
            if course["Title"].lower() == course_title.lower():  # Case-insensitive matching
                self.courses.append(course)
                return True
        print(f"Course '{course_title}' not found.")
        return False

    def print_courses(self):
        """
        Display all courses enrolled by the student.
        """
        if self.courses:
            print("Enrolled Courses:")
            for course in self.courses:
                print(course['Title'])
        else:
            print("This student has no enrolled courses.")


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

    def add_course(self, course_title, teacher_name):
        """
        Add a new course to the system.
        
        Args:
            course_title (str): Title of the new course
            teacher_name (str): Name of the teacher for the course
            
        Returns:
            bool: True if course added successfully, False otherwise
        """
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
