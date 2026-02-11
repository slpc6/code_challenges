"""Find the Torsional Angle"""

import math

class Points:
    """"Class to defin a 3d point"""
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

    def dot(self, no):
        """Return the dot product
        
        """
        return((self.x * no.x) + (self.y * no.y) + (self.z * no.z))

    def cross(self, no):
        """Return the cross product
        
        """
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    def absolute(self):
        """Return the absolute value
        
        """
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = []
    for i in range(4):
        a = map(float, input().split())
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    X = (b - a).cross(c - b)
    Y = (c - b).cross(d - c)
    angle = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))
    print(f"{math.degrees(angle):.2f}")
