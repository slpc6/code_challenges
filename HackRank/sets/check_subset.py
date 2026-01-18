""""check subset"""

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        Len_A = int(input())
        A = set(map(int, input().split()))
        Len_B = int(input())
        B = set(map(int, input().split()))
        print(A.issubset(B))
