class Student:
    school_name = "Willes Little Flower School and Collage"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"School Name: {Student.school_name}")
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")

student_1 = Student("Ahan", "10th Grade")
student_1.display_info()
student_2 = Student("Wachiu", "10th Grade")
student_2.display_info()
student_3 = Student("Saminur", "10th Grade")
student_3.display_info()



print("------------------------------------------------------------")




class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

rectangle = Rectangle(25, 8)
print(f"Length: {rectangle.length}")    # Output: Length: 25
print(f"Width: {rectangle.width}")      # Output: Width: 8
print(f"Area: {rectangle.area}")        # Output: Area: 200




print("------------------------------------------------------------")




class Circle:
    @staticmethod
    def calculate_area(radius):
        return 3.14 * radius ** 2

    @classmethod
    def description(cls):
        return "This is a class to represent a circle and calculate its area."

print(Circle.calculate_area(25))  # Output: 1962.5
print(Circle.description())      # Output: This is a class to represent a circle and calculate its area.
