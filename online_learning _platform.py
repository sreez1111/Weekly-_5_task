from abc import ABC, abstractmethod

# Abstract Base Class
class Course(ABC):

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


# Subclass 1: Programming Course
class ProgrammingCourse(Course):

    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Category: Programming 💻")
        print("Includes coding projects and practical sessions.")


# Subclass 2: Design Course
class DesignCourse(Course):

    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Category: Design 🎨")
        print("Focuses on creativity, UI/UX, and visual skills.")


# Subclass 3: Marketing Course
class MarketingCourse(Course):

    def course_details(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Category: Marketing 📈")
        print("Covers digital marketing and business strategies.")


# Creating objects
prog = ProgrammingCourse("Python Full Stack", "6 Months")
design = DesignCourse("Graphic Design Mastery", "4 Months")
market = MarketingCourse("Digital Marketing Pro", "3 Months")

courses = [prog, design, market]

# Display course details
for course in courses:
    course.course_details()
    print("----------------------------")