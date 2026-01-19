"""Symmetric Difference"""

if __name__ == '__main__':
    M = int(input())
    S1 = set(map(int, input().split()))
    N = int(input())
    S2 = set(map(int, input().split()))

    dif = sorted(S1.symmetric_difference(S2))
    print(*(i for i in dif), sep='\n')
