import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def scale(self, s):
        self.x *= s
        self.y *= s

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        m = self.magnitude()
        if m != 0:
            self.x /= m
            self.y /= m