"""Counter"""

from collections import Counter

n_shoes = int(input())
s_shoes = Counter(map(int, input().split()))
customers = int(input())
TOTAL = 0
for i in range(customers):
    size, price = map(int, input().split())
    if s_shoes[size]:
        s_shoes[size] -= 1
        TOTAL += price
print(TOTAL)
