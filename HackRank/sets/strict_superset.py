"""Strict superset"""


if __name__ == '__main__':
    A = set(map(int, input().split()))
    RES = True
    for _ in range(int(input())):
        S = set(map(int, input().split()))
        if not A > S:
            RES = False
    print(RES)
