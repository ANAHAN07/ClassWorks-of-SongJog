class Student:
    def __init__(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

student = Student(69)
print(student.get_grade())  # Output: 69



print("==================================================")



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_info(self):
        print(f'''
Name: {self.name}
age: {self.age}
grade: {self.grade}
                ''')

    # def get_grade(self):
    #     return f"{self.name} is in grade {self.grade}."

student = Student("Ahan", 17, 10)
# print(student.introduce())  # Output: My name is Ahan, and I am 17 years old.
print(student.display_info())  # Output: Ahan is in grade 10.