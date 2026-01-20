"""Polar Coordinates"""

from cmath import phase
import math


if __name__ == '__main__':
    num = complex(input())
    r = math.sqrt(pow(num.real, 2) + pow(num.imag, 2))
    y = phase(num)
    print(r, y, sep='\n')
