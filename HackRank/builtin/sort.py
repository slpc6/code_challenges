"""ginortS"""

string = list(input())
string.sort(key=lambda x: (x.isdigit() - x.islower(), x.isdigit() and int(x) % 2 == 0, x))
print(''.join(i for i in string))
