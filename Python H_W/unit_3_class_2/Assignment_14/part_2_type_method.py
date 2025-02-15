class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def is_square(length, width):
        return length == width

    @classmethod
    def description(cls):
        return "This class handles rectangles."

    def area(self):
        return self.length * self.width

rect1 = Rectangle(25, 25)
print(Rectangle.is_square(69, 65))         # Output: False 
print(Rectangle.description())          # Output: This class handles rectangles.
print(rect1.area())                     # Output: 625
