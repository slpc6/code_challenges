"""Any or all"""

N = int(input())
ls = list(map(int, input().split()))
print(all(
    map(lambda x: x>0, ls)) and
    any(map(lambda x: str(x) == str(x)[::-1], ls)))
