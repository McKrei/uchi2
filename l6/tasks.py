class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Человек: {self.name}'

    def get_age(self):
        return f'Возраст: {self.age}'


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def get_name(self):
        return f'Ученик: {self.name} ({self.course} класс)'


name = input()
age = input()
course = input()
student = Student(name, age, course)
print(student.get_name())
print(student.get_age())






class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D:
    pass


class E(B, C, D):
    pass

print(E.__mro__)





class Queue(list):
    def front(self):
        elem = self.pop(0)
        return f'Ушел из очереди: {elem}. В очереди: {", ".join(self)}'

    def get_info(self):
        return f'В очереди {len(self)} человек: {", ".join(self)}. Следующий в очереди: {self[0]}'


lst = Queue()
for _ in range(int(input())):
    lst.append(input())
print(lst.front())
print(lst.front())
print(lst.get_info())
