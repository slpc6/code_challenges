"""Company Logo"""

from collections import Counter


if __name__ == '__main__':
    s = input()
    l = sorted(Counter(s).items(), key=lambda item: (-item[1], item[0]))
    print(*[f"{item[0]} {item[1]}" for item in l[:3]], sep='\n')
