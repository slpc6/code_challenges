"""Word order"""

from collections import OrderedDict

dic = OrderedDict()

for i in range(int(input())):
    word = input()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print(len(dic))
for count in dic.values():
    print(count, end=' ')
