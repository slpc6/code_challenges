"""The captain's room"""


from collections import Counter


if __name__ == '__main__':
    group_size = int(input())
    rooms_list = map(int, input().split())
    counts = Counter(rooms_list)
    for room, count in counts.items():
        if count != group_size:
            print(room)
