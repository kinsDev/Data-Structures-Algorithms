# Challenge 2: Implement an Animal Class

class Animal:
    def __init__(self, name, sound): # initializing properties
        self.name = name
        self.sound = sound
    
    def Animal_details(self):
        print("Name:", self.name)
        print("Sound:", self.sound)

# Hierarchical Inheritance
class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family
    
    def Animal_details(self): # overridden method
        super().Animal_details()
        print("Family", self.family)

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color
    
    def Animal_details(self): # overridden method
        super().Animal_details()
        print("Color:", self.color)

d = Dog("Pongo", "woof woof", "Husky") # object d in the Dog class with its defined attrbutes
d.Animal_details() # printing d it using the printing method from the Dog class which is a child of the Animal parent class
print("\n")
s = Sheep("Billy", "Baa Baa", "White")
s.Animal_details()
