'''
1.	Создай класс Point (точка в пространстве) без атрибутов.
Добавь метод set_coordinates, который будет добавлять объекту атрибуты x, y, z, а также метод get_coordinates, который будет возвращать кортеж значений атрибутов x, y, z.

Считай с клавиатуры 3 целых числа: x, y, z - каждое на отдельной строке и создай экземпляр класса Point. Используя методы добавь объекту атрибуты со значениями которые ты считал с клавиатуры. Используя методы выведи кортеж содержащий значения атрибутов объекта, а также используя специальную переменную __dict__ выведи на экран на новой строке все атрибуты объекта.

Входные данные:
Вводится 3 целых числа - каждое на новой строке.

Выходные данные:
Вводится кортеж и вводятся все атрибуты объекта на разных строках.
'''









class Point:
    def set_coordinates(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return self.x, self.y, self.z


x = int(input())
y = int(input())
z = int(input())

pt = Point()
pt.set_coordinates(x, y, z)
print(pt.get_coordinates())
print(pt.__dict__)




















'''
2.	Создай класс Circle (окружность на плоскости) без атрибутов.
Добавь метод set_center, который будет добавлять объекту атрибуты x, y и метод set_radius, который будет добавлять объекту атрибут R. Также добавь метод get_distance - который будет возвращать расстояние от начала координат до центра окружности с точностью до сотых и get_area, который будет возвращать площадь круга ограниченного данной окружностью с точностью до сотых.

Считай с клавиатуры 3 целых числа: x, y, R - каждое на отдельной строке и создай экземпляр класса Circle . Используя методы добавь объекту атрибуты со значениями которые ты считал с клавиатуры. Используя методы выведи площадь круга ограниченного данной окружностью и расстояние от начала координат до центра окружности с точностью до сотых на разных строках.

Входные данные:
Вводится 3 целых числа - каждое на новой строке.

Выходные данные:
Вводится площадь и расстояние округленные до сотых на разных строках.

import math
'''

class Circle:
    def set_center(self, x, y):
        self.x = x
        self.y = y

    def set_radius(self, R):
        self.R = R

    def get_distance(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def get_area(self):
        return round(3.14 * self.R ** 2, 2)


x = int(input())
y = int(input())
R = int(input())

c = Circle()
c.set_center(x, y)
c.set_radius(R)
print(c.get_area())
print(c.get_distance())

'''
3.	Создай класс Student с атрибутом MAX_LENGTH = 20. Добавь метод validate_length с использованием @classmethod  который будет проверять что длина имени студента не должна превышать значение атрибута MAX_LENGTH. Добавь метод validate_name с использованием @staticmethod который будет проверять, что имя студента состоит только из букв. Оба метода должны возвращать True или False.

Считай с клавиатуры одну строку - имя студента. Выведи результат метода validate_length и validate_name  для данного имени на разных строках.

Входные данные:
Вводится одна строка - имя.

Выходные данные:
Вводится True или False два раза на разных строках.
'''
class Student:
    MAX_LENGTH = 20

    @classmethod
    def validate_length(cls, name):
        return len(name) <= cls.MAX_LENGTH

    @staticmethod
    def validate_name(name):
        return name.isalpha()


name = input()
print(Student.validate_length(name))
print(Student.validate_name(name))












'''
4.	Создай класс Polygon (многоугольник) без атрибутов.
Добавь метод set_vertices_count, который будет добавлять объекту атрибут count - количество вершин и метод set_coordinates, который будет добавлять объекту атрибут coords - список кортежей координат многоугольника. Реализуй метод get_side_length, который будет принимать в качестве параметра номер стороны и будет возвращать длину стороны этого многоугольника с точностью до сотых.

Считай с клавиатуры одно целое число n - количество вершин, затем считай n пар целых чисел x, y - координаты вершин многоугольника. Создай экземпляр класса, используя методы добавь объекту атрибуты со значениями которые ты считал с клавиатуры.

Считай с клавиатуры номер стороны и используя метод get_side_length выведи длину этой стороны с точностью до сотых.

Входные данные:
Вводится одно целое число n - количество вершин.
Затем вводятся n пар целых чисел через пробел - координаты x y.
Вводится номер стороны (нумерация начинается с 1).

Выходные данные:
Выводится длина стороны с точностью до сотых.
'''

class Polygon:

    def set_vertices_count(self, count):
        self.count = count

    def set_coordinates(self, coords):
        self.coords = coords

    def get_side_length(self, num):
        if num == self.count:
            length = ((self.coords[0][0] - self.coords[num - 1][0]) ** 2 +
                        (self.coords[0][1] - self.coords[num - 1][1]) ** 2) ** 0.5
        else:
            length = ((self.coords[num][0] - self.coords[num - 1][0]) ** 2 +
                        (self.coords[num][1] - self.coords[num - 1][1]) ** 2) ** 0.5

        return round(length, 2)

n = int(input())
coords = []
for _ in range(n):
   x, y = map(int, input().split())
   coords.append((x, y))

polygon = Polygon()
polygon.set_vertices_count(n)
polygon.set_coordinates(coords)
print(polygon.get_side_length(1))
print(polygon.get_side_length(4))
