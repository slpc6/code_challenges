"""Athlete Sort"""

if __name__ == '__main__':
    N, M = map(int, input().split())

    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().rstrip().split())))

    K = int(input().strip())
    for i in sorted(arr, key=lambda x: x[K]):
        print(' '.join(str(item) for item in i))
