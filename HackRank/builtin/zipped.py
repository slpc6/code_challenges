"""Zipped"""
students, subject = map(int, input().split())
result = []
for _ in range(subject):
    result.append(list(map(float, input().split())))
scores = zip(*result)
for i in scores:
    print(f'{(sum(i)/subject):.1f}')
