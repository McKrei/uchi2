class Student:
    def __init__(self, name, course):
        self.__name = name
        self.__status = 'student'
        self.__course = course

    def next_course(self):
        if self.__course <= 10:
            self.__course += 1
        else:
            self.__course = None
            self.__status = 'graduate'

    def deduction(self):
        self.__course = None
        self.__status = 'expelled'

    def get_info(self):
        return f'Student: {self.__name} ({self.__course}), status: {self.__status}'


name = input()
course = int(input())
student = Student(name, course)
method = input()
if method == 'next_course':
    student.next_course()
elif method == 'deduction':
    student.deduction()
print(student.get_info())
