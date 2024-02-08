class Point:
    MIN = -100
    MAX = 100
    DEFAULT_VALUE = 0

    @classmethod
    def __correct_value(cls, value):
        return value if cls.MIN <= value <= cls.MAX else cls.DEFAULT_VALUE

    def __init__(self, x, y):
        self.__x = self.__correct_value(x)
        self.__y = self.__correct_value(y)

    def set_x(self, x):
        self.__x = self.__correct_value(x)

    def set_y(self, y):
        self.__y = self.__correct_value(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


point1 = Point(20, 90)
print(point1.get_x(), point1.get_y())
point1.set_x(1000)
point1.set_y(50)
print(point1.get_x(), point1.get_y())
