class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

temp = Temperature(45)
print(temp.fahrenheit)  # Output: 113.0
