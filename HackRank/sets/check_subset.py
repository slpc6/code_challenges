""""check subset"""

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        len_a = int(input())
        a = set(map(int, input().split()))
        len_b = int(input())
        b = set(map(int, input().split()))
        print(a.issubset(b))
