class Alien:
    def __init__(self, color, heart=0):
        self.color = color
        self.heart = heart
        self.damage = 5

def can_fire(self):
    if self.color == "black":
        return True
    else: return False

def fire(self, hero):
    hero.health -= self.damage


class Hero:
    def __init__(self, health=150):
        self.health = health
        self.damage = 10

    def fire(self, alien):
        alien.heart -= self.damage

alien_1 = Alien("red,15")
print(f"Alien-1 Heart: {alien_1.heart}")
alien_2 = Alien("black,20")
print(f"Alien-2 Heart: {alien_2.heart}")


