"""Named Tuple"""

from collections import namedtuple

n_students = int(input())
Student = namedtuple('Student', list(input().split()))
result = 0
for i in range(n_students):
    std = Student(*input().split())
    result += int(std.MARKS)
print(f'{result/n_students:.2f}')
