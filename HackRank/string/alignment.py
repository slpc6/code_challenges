"""älignment"""

thickness = int(input())
C = 'H'

for i in range(thickness):
    print((C*i).rjust(thickness-1)+C+(C*i).ljust(thickness-1))


for i in range(thickness+1):
    print((C*thickness).center(thickness*2)+(C*thickness).center(thickness*6))


for i in range((thickness+1)//2):
    print((C*thickness*5).center(thickness*6))


for i in range(thickness+1):
    print((C*thickness).center(thickness*2)+(C*thickness).center(thickness*6))


for i in range(thickness):
    print(((C*(thickness-i-1)).rjust(thickness)+C+
    (C*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
