"""Piling Up"""

for _ in range(int(input())):
    size = int(input())
    blocks = list(map(int, input().split()))
    stack = []
    for _ in range(size):
        if blocks[0] > blocks[-1]:
            stack.append(blocks[0])
            blocks.pop(0)
        else:
            stack.append(blocks[-1])
            blocks.pop(-1)

    if stack == sorted(stack, reverse=True):
        print("Yes")
    else:
        print("No")
