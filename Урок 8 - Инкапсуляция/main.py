

class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport

    def info(self):
        print(self.__dict__)

    def __getattribute__(self, items):
        ...

    def __setattr__(self, key, value):
        self.__dict__[key] = value


        # return

p = Person('Ваня', 27, 112155)
p.name = 'Петя'
print(p.name)
# print(p.name)
# print(per.__dict__)
