""""Set Mutation"""

if __name__ == '__main__':
    N = int(input())
    data = set(map(int, input().split()))
    for _ in range(int(input())):
        command = input().split()
        match command[0]:
            case "intersection_update":
                new_data = set(map(int, input().split()))
                data.intersection_update(new_data)
            case "update":
                new_data = set(map(int, input().split()))
                data.update(new_data)
            case "symmetric_difference_update":
                new_data = set(map(int, input().split()))
                data.symmetric_difference_update(new_data)
            case "difference_update":
                new_data = set(map(int, input().split()))
                data.difference_update(new_data)
    print(sum(data))
