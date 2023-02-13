# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Mammal(Animal):
#     def __init__(self, name):
#         super().__init__(name)

# class Bird(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "чик чирик!"

# class Dog(Mammal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "Woof!"

# class Cat(Mammal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "Meow"

# class Parrot(Bird):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "Polly wants a cracker"

# class Gopnik(Mammal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return "Blyat!"




class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

class Gopnik(Animal):
    def speak(self):
        return "Blin, nu i che?"

animals = [Dog("Buddy"), Cat("Whiskers"), Cow("Betsy"), Gopnik("Seryoga")]

for animal in animals:
    print(animal.name + " says " + animal.speak())
