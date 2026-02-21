"""Reduce Function"""

from fractions import Fraction
from functools import reduce

def product(frac_list: list) -> tuple:
    """Calculate the multipli of all fractions in
    the list
    """
    t = reduce(lambda x, y: x*y, frac_list)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
