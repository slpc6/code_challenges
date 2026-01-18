"""add"""

if __name__ == '__main__':
    N = int(input())
    res = set[str]()
    for i in range(N):
        res.add(input().strip())
    print(len(res))
