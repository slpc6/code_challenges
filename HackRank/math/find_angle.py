""""Find the angle MBC"""


import math


if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    angle = math.degrees(math.atan(AB/BC))
    print(f"{angle:.0f}°")
