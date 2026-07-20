from abc import ABC, abstractmethod
import math

class Shape(ABC):
    count = 0
    def __init__(self):
        Shape.count += 1

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @classmethod
    def total_shapes(cls):
        print("Total Shapes Created:", cls.count)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

def print_report(shapes_list):
    print("----- Shape Report -----")
    for shape in shapes_list:
        print("Shape:", shape.__class__.__name__)
        print("Area =", round(shape.area(), 2))
        print("Perimeter =", round(shape.perimeter(), 2))
        print()

c1 = Circle(7)
r1 = Rectangle(10, 5)
t1 = Triangle(3, 4, 5)

shapes = [c1, r1, t1]
print_report(shapes)
Shape.total_shapes()