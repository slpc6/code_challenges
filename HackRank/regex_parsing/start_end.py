"""Start End"""

import re

S = input()
k = input()

matches = list(re.finditer(f'(?={k})', S))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))
