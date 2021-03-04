class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def triangle_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** (1./2)

    def __str__(self):
        return "Triangle: SideA = {}, SideB = {}, SideC = {}".format(self.side_a, self.side_b, self.side_c)