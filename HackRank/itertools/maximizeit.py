"""Maximize it"""

from itertools import product

K, M = map(int,input().split())
lists = []
for i in range(K):
    L = list(map(int, input().split()))
    L.pop(0)
    lists.append(L)

count = 0
for com in product(*lists):
    total = sum(pow(x, 2) for x in com) % M
    if total > count:
        count = total
print(count)
