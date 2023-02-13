
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'точка {self.x}'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __len__(self):
        return len(self.cord)

    def __bool__(self):
        return self.x >= 100



s = '123,4124\n241,314\n24,3413\n31,41'
points = [Point(*el)for el in [tuple(map(int, i.split(','))) for i in s.split('\n')]]
print(points)
# if p:
#     print('Hello')
# else:
#     print('World')

# points = [p]
lst = [el for el in points if el]
print(lst)
