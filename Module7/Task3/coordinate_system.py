import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

point1 = Point(1, 1)
point2 = Point(2, 2)

print(point1.distance_from_xy(2, 2))   # Output: 1.4142135623730951
print(point1.distance_from_point(point2))  # Output: 1.4142135623730951
