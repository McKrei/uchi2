# class Student:
#     def __init__(self, name):
#         self.name=name

#     def get_action(self):
#         return f'Ученик {self.name} учится'

# class Teacher(Student):
#     def __init__(self, name):
#         super().__init__(name)
#     def get_action(self):
#         return f'Учитель {self.name} учит'

# n=int(input())
# s=[]
# for _ in range(n):
#     b=input().split()
#     if b[0]=='Student:':
#         c=Student(b[1: ])

#         print(c.get_action())
#     elif b=='Teacher:':
#         c=Teacher(d)

##### ВЕРНЫЙ ВАРИАНТ
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class Student(Person):
    def get_action(self):
        return f'Ученик {self.name} учится'


class Teacher(Person):
    def get_action(self):
        return f'Учитель {self.name} учит'
    

n = int(input())
persons = []
for i in range(n):
    line = input().split(': ')
    if line[0] == 'Student':
        obj = Student(line[1])
    else:
        obj = Teacher(line[1])
    persons.append(obj)
print(persons)
for person in persons:
    print(person.get_action())
