"""Iterables and Iterators"""


from itertools import combinations

N = int(input())
letters = list(input().split())
k = int(input())

comb = list(combinations(letters, k))

count = 0
for i in comb:
    if 'a' in i:
        count += 1

print(f"{count/len(comb):.12f}")
