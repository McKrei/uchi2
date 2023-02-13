import math

class Circle:
    def set_center(self, x, y):
        self.x = x
        self.y = y

    def set_radius(self, R):
        self.R = R

    def get_distance(self):
        return round(math.sqrt(self.y ** 2 + self.x ** 2), 2)

    def get_area(self):
        return(2 * 3.14 * self.R ** 2)


a = Circle()
x,y,R = int(13), int(14), int(15)
a.set_center(x,y)
a.set_radius(R)
print(a.get_area())
print(a.get_distance())

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


x,y,R = int(13), int(14), int(15)

c = Circle()
c.set_center(x, y)
c.set_radius(R)
print(c.get_area())
print(c.get_distance())
