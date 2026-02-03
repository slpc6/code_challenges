"""deque"""

from collections import deque

dq = deque()
for i in range(int(input())):
    S = input().split()
    match S[0]:
        case 'append':
            dq.append(int(S[1]))
        case 'appendleft':
            dq.appendleft(int(S[1]))
        case 'pop':
            dq.pop()
        case 'popleft':
            dq.popleft()

print(*dq)
