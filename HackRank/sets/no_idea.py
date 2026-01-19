"""no idea"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    H = 0
    H += sum(1 for i in l if i in a) - sum(1 for i in l if i in b)
    print(H)
