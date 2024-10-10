class Dog:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print(f"My name is {self.name} and i can Bark.")

class Cat:
    def __init__(self,name):
      self.name = name

    def make_sound(self):
        print(f"My name is {self.name} and i  can Meow.")

        #Object
Lucky = Dog("Lucky")
Fuzzy = Cat("Fuzzy")

        #Polymorphism
pets = (Lucky,Fuzzy)

for pet in pets:
    pet.make_sound()
