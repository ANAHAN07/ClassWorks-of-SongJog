class Shapes:
    def __init__(self):
        pass
    def calculate_area(self):
        print("Calculating Area!")

class Circle(Shapes):
    def __init__(self, radious):
        self.radious = radious

    def calculate_area(self):
        return 3.1416 * self.radious**2

class Square(Shapes):
    def __init__(self, lenght):
        self.lenght = lenght

    def calculate_area(self):
        return self.lenght**2
    

c_1 = Circle(10)
s_1 = Square(15)

print(c_1.calculate_area())     # Output: 314.15999999999997
print(s_1.calculate_area())     # Output: 225