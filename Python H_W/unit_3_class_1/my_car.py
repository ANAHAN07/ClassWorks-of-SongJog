class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def output(self):
        print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nColor: {self.color}")


my_car = Car("Toyota", "Harrier", "Wine Red")
my_car_1 = Car("Honda", "CHR", "Pearl")
my_car_3 = Car("Honda", "CRV", "Black")
my_car.output()
my_car_1.output()
my_car_3.output()