class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"The {self.species} goes '{self.sound}'.")                           # Output: The dog goes 'vao vao'.
                                                                                    # Output: The cat goes 'meow meow meowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'.

dog = Animal("dog", "vao vao")
dog.make_sound()

cat = Animal("cat", "meow meow meowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
cat.make_sound()