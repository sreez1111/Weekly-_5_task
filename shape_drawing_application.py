from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def draw(self):
        print("Drawing a Circle ⚪")


# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a Rectangle ▭")


# Triangle Class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing a Triangle 🔺")


# Creating Objects
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculating Areas
print("Circle Area:", circle.area())
circle.draw()

print("Rectangle Area:", rectangle.area())
rectangle.draw()

print("Triangle Area:", triangle.area())
triangle.draw()