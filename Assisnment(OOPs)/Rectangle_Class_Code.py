class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)
rect3 = Rectangle(7, 7)

print("Rectangle 1")
print("Area =", rect1.area())
print("Perimeter =", rect1.perimeter())

print("\nRectangle 2")
print("Area =", rect2.area())
print("Perimeter =", rect2.perimeter())

print("\nRectangle 3")
print("Area =", rect3.area())
print("Perimeter =", rect3.perimeter())