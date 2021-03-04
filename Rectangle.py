class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeigh(self):
        return self.height

    def getArea(self):
        return self.width * self.height


class Square:

    def __init__(self, side):
        self.side = side

    def get_area_square(self):
        return self.side ** 2


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        return 3.14 * (self.radius ** 2)