class Point:
    MIN = -100
    MAX = 100

    def __init__(self, x, y):
        # self.x = self.y = 0
        self.x = x
        self.y = y

        # if self.MIN <= x <= self.MAX:
        # if self.MIN <= y <= self.MAX:

    @staticmethod
    def sum_points(p1, p2):
        return Point(
            p1.x + p2.x,
            p1.y + p2.y
        )

    @classmethod
    def sum_points_with_check(cls, p1, p2):
        result_x = p1.x + p2.x
        result_y = p1.y + p2.y
        return Point(
            result_x if result_x <= cls.MAX else cls.MAX,
            result_y if result_y <= cls.MAX else cls.MAX,
        )

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'


point1 = Point(20, 90)
point2 = Point(10, 40)
point3 = Point.sum_points(point1, point2)
point4 = Point.sum_points_with_check(point1, point2)
print(point1)
print(point2)
print(point3)
print(point4)
