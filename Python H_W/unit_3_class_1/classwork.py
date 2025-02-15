class car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def fastest(self, speed):
        if speed >= 150:
            print(f"The {self.brand} {self.model} is the fastest car.")
        else:
            print(f"The {self.brand} {self.model} is not fastest")

    def electric_t(self):
        if self.brand == "Tesla":
            print(f"This is an electric car!")
        else:
            print(f"This car is not an electric car!")


lamborgini = car("Hurracan", "Avantador", "SVJ363")
lamborgini.fastest(450)
lamborgini.electric_t()
    
