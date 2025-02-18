# Implementing Polymorphism Using Duck Typing

# Using duck typing, we can implement polymorphism without using inheritance.
# Duck typing extends the concept of dynamic typing in Python.
# Dynamic typing means that we can change the type of an object later in the code.


# Due to the dynamic nature of Python, duck typing allows the user to use any object 
# that provides the required behavior without the constraint that it has to be a subclass. 
# See the code below for a better understanding of dynamic typing in Python:

x = 7 # type of X is an integer. X is also an object here
print(type(x))

x = "Kinsley" # the same object has been assigned something different, this time a string using the same previuosly used class
print(type(x))



# Implementing duck typing
class Dog:
    def Speak(self):
        print("Woof woof")

class Cat:
    def Speak(self):
        print("Meow meow")

class AnimalSound:
    def Sound(self, animal):
        animal.Speak() # calling the methods in other classes

sound = AnimalSound() # object in the AnimalSound class
dog = Dog() # object in the Dog class
cat = Cat() # oject in the Cat class

sound.Sound(dog)
sound.Sound(cat)
# sound is an instance of AnimalSound.
# sound expects an argument animal, and here dog(which is an instance of Dog) is passed
# Inside Sound, animal.Speak() is executed. Since animal is a dog, dog.speak() is called, printing "woof woof" 



# In layman terms, since both the animals, dog and cats, can speak like animals, 
# they both are animals. This is how we have achieved polymorphism without inheritance.
