class Shape:
    def __str__(self):
        return self.__class__.__name__


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimter(self):
        return 2 * (self.a + self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(3.14 * self.r ** 2)

    def get_perimter(self):
        return round(2 * 3.14 * self.r)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)

    def get_perimter(self):
        return self.a + self.b + self.c


class RightTriangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return round(self.a * self.b / 2)

    def get_perimter(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return round(self.a + self.b + c)


s = input()
if s == 'Rectangle':
    a, b = map(int, input().split())
    shape = Rectangle(a, b)
elif s == 'Circle':
    r = int(input())
    shape = Circle(r)
elif s == 'Triangle':
    a, b, c = map(int, input().split())
    shape = Triangle(a, b, c)
else:
    a, b = map(int, input().split())
    shape = RightTriangle(a, b)
print(shape)
print(shape.get_area())
print(shape.get_perimter())


import math

class Shape:
    def __init__(self, *args):
        self.args = args

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Rectangle(Shape):
    def get_area(self):
        return round(self.args[0] * self.args[1])

    def get_perimeter(self):
        return round(2 * (self.args[0] + self.args[1]))

class Circle(Shape):
    def get_area(self):
        return round(math.pi * self.args[0] ** 2)

    def get_perimeter(self):
        return round(2 * math.pi * self.args[0])

class Triangle(Shape):
    def get_area(self):
        a, b, c = self.args
        s = (a + b + c) / 2
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)))

    def get_perimeter(self):
        return round(sum(self.args))

class RightTriangle(Triangle):
    def get_area(self):
        a, b = self.args
        return round(a * b / 2)

    def get_perimeter(self):
        a, b = self.args
        c = math.sqrt(a ** 2 + b ** 2)
        return round(a + b + c)

shape_name = input().strip()
shape_args = list(map(int, input().strip().split()))

if shape_name == 'Rectangle':
    shape = Rectangle(*shape_args)
elif shape_name == 'Circle':
    shape = Circle(*shape_args)
elif shape_name == 'Triangle':
    shape = Triangle(*shape_args)
elif shape_name == 'RightTriangle':
    shape = RightTriangle(*shape_args)

print(shape)
print(shape.get_area())
print(shape.get_perimeter())
