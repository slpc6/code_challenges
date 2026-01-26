"""Compress the string"""

from itertools import groupby

lis = map(int, input())

for i, j in groupby(lis):
    n = len(list(j))
    print((n, i), end=' ')
