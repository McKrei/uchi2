# class Point:
#     def __init__(self):
#         self.__x = 0
#         self.__y = 0

#     def __getattribute__(self, item):
#         return super().__getattribute__(item)

#     def __setattr__(self, name, value):
#         if value >= 0:
#             super().__setattr__(name, value)
#         else:
#             print('Координата должна быть > 0')

#     def __str__(self):
#         return f'Point ({self.__x}, {self.__y})'


class Point:
    def __init__(self):
        self._x = 0
        self._y = 0
    def newx(self,newx):
        if newx < 0:
            print('Координата должна быть >= 0')
        else:
            self._x = newx
    def newy(self, newy):
        if newy < 0:
            print('Координата должна быть >= 0')
        else:
            self._y = newy
    def __str__(self):
        return f'Point ({self._x}, {self._y})'
a = input().split()
b = list(map(int, a))
ex = Point()
ex.newx(b[0])
ex.newy(b[1])
print(ex)



# class Point:
#     def __init__(self):
#         self.__x = 0
#         self.__y = 0

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, value):
#         if value >= 0:
#             self.__x = value
#         else:
#             print('Координата должна быть > 0')

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, value):
#         if value >= 0:
#             self.__y = value
#         else:
#             print('Координата должна быть > 0')

#     def __str__(self):
#         return f'Point ({self.__x}, {self.__y})'



# x, y = map(int, input().split())
# point = Point()
# point.x = x
# point.y = y
# print(point)
