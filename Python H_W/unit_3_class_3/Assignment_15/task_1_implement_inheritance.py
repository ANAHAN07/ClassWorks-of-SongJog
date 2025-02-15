class Vehicle:
    def __init__(self, brand, model, year, type):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = type
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, type, fuel_type):
        super().__init__(brand, model, year, type)
        self.fuel_type = fuel_type
    
    def display_info(self):
        print(f"Brand: {self.brand},Model: {self.model}, Type: {self.type} Year: {self.year}, Fuel Type: {self.fuel_type}")

car_1 = Car("BMW", "M3 Competition xDrive", 2024, "Sedan", "Gasoline")
car_1.display_info()    # Output: Brand: BMW,Model: M3 Competition xDrive, Type: Sedan Year: 2024, Fuel Type: Gasoline

car_1 = Car("BMW", "M4 Competition Coupe", 2024, "Sedan", "Petrol (RON 95)")
car_1.display_info()    # Output: Brand: BMW,Model: M4 Competition Coupe, Type: Sedan Year: 2024, Fuel Type: Petrol (RON 95)

car_1 = Car("BMW", "M8 Competition Gran Coupe", 2020, "Sedan", "Petrol (RON 95)")
car_1.display_info()    # Output: Brand: BMW,Model: M8 Competition Gran Coupe, Type: Sedan Year: 2020, Fuel Type: Petrol (RON 95)
