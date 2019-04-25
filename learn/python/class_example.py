class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    PI = 3.14

    def __init__(self, center, r):
        self.center = center
        self.r = r

    def get_area(self):
        return self.r ** 2 * Circle.PI

    def get_perimeter(self):
        return self.r * Circle.PI * 2

    def get_center(self):
        return self.center.x, self.center.y

    def print(self):
        print(f'Circle: {(self.center.x, self.center.y)}, r: {self.r}')


p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()

"""
28.26
18.84
(0, 0)
Circle: (0, 0), r: 3
3.14
6.28
(4, 5)
Circle: (4, 5), r: 1
"""
