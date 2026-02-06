"""Default dict tutorial"""

from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)
for i  in range(n):
    d[input()].append(i+1)

for i in range(m):
    word = input()
    if word in d:
        print(*d[word])
    else: print(-1)
