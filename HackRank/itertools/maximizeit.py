"""Maximize it"""

from itertools import product

K, M = map(int,input().split())
lists = []
for i in range(K):
    l = list(map(int, input().split()))
    l.pop(0)
    lists.append(l)

max_mod = 0
for com in product(*lists):
    total = sum(pow(x, 2) for x in com) % M
    if total > max_mod:
        max_mod = total
print(max_mod)
