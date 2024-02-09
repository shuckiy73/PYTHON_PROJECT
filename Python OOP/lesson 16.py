

class IntegerCoordinate:
    @staticmethod
    def validate_point(num):
        return num if type(num) == int else 0

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, self.validate_point(value))


class Point:
    x = IntegerCoordinate()
    y = IntegerCoordinate()
    z = IntegerCoordinate()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point1 = Point(1, 2, 'ndrthdt')
point2 = Point(100, 50, -20)
print(point1.__dict__)
print(point2.__dict__)
print(point2.x)
point2.x = 88
print(point2.x)
print(point2.__dict__)
