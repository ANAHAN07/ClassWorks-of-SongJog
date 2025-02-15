class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return "Some birds can fly"

class Eagle(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        return "Can fly"

class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        return "Cannot fly"

eagle = Eagle("Eagle")
penguin = Penguin("Penguin")

print(f"{eagle.name}: {eagle.fly()}")   # Output: Eagle: Can fly
print(f"{penguin.name}: {penguin.fly()}") # Output: Penguin: Cannot fly



from abc import ABC, abstractmethod

class Appliance(ABC):  
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):  
    def turn_on(self):
        return "Fan is now on"

class TV(Appliance):  
    def turn_on(self):
        return "TV is now on"

fan = Fan()
tv = TV()

print(fan.turn_on())  # Output: Fan is now on
print(tv.turn_on())   # Output: TV is now on