"""Ordered Dict"""

from collections import OrderedDict

dic = OrderedDict()

for i in range(int(input())):
    item_name, space, net_price = input().rpartition(' ')
    if item_name in dic:
        dic[item_name] += int(net_price)
    else:
        dic[item_name] = int(net_price)

for item_name, net_price in dic.items():
    print(item_name, net_price)
