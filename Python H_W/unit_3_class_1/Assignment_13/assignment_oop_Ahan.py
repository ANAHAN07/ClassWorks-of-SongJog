class Person:       
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")          # Output: Hello, My name is Alauddin and I am 17 years old.

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")         # Output: Hello, My name is Wachiu and I am 15 years old.

    def share_hobby(self):
        print(f"Hi, I am {self.name} and I love {self.hobby}.")                     # Output: Hi, I am Ahnaf and I love Playing Games.

person_1 = Person("Alauddin", 17, "Reading")
person_1.greet()

person_2 = Person("Wachiu", 15, "Singing")
person_2.greet()

person = Person("MADARA", 90, "Fighting")
person.greet()
person.birthday()

person_3 = Person("Ahnaf", 99, "Playing Games")
person_3.share_hobby()