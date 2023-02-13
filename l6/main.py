class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return f'Человек: {self.name}'

    def get_age(self) -> str:
        return f'Возраст: {self.age}'


class Student(Person):
    def __init__(self, name: str, age: int, course: int):
        super().__init__(name, age)
        self.course = course

    def get_name(self):
        return f'Ученик: {self.name} ({self.course} класс)'

student_name = input()
student_age = int(input())
student_course = int(input())

stud = Student(student_name, student_age, student_course)
print(stud.get_name())
print(stud.get_age())
