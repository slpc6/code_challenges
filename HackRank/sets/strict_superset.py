"""Strict superset"""


if __name__ == '__main__':
    a = set(map(int, input().split()))
    result = True
    for _ in range(int(input())):
        s = set(map(int, input().split()))
        if not a > s:
            result = False
    print(result)
