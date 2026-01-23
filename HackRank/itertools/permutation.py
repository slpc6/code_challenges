""""Make permutations"""

from itertools import permutations

data = input().split()
perm = permutations(data[0], int(data[1]))
for i in sorted(perm):
    print(''.join(i))
