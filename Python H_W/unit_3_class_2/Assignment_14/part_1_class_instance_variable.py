class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Wheels: {Car.wheels}")        # Output: Brand: BMW, Model: M5 Competition CS, Wheels: 4

car1 = Car("BMW", "M5 Competition CS")
car1.display_info()
