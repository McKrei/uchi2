class Point:
    def __init__(self, *args):
        self.coords = args

    def __str__(self):
        return f'Точка с координатами {self.coords}'


coords = map(int, input().split())
my_point1 = Point(*coords)
print(my_point1)
