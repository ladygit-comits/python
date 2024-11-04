#Parent class/super class/ base class
class animals:
    def speak(self):
        print("Animal is speaking")

#Child class/ sub class
class dog(animals):
    def bark(self):
        print("Dog is barking")

a = animals()

d = dog()
d.speak()
