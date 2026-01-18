"""discard, remove and pop"""

if __name__ == '__main__':
    len_s = int(input())
    S = set(map(int, input().split()))
    len_commands = int(input())
    for _ in range(len_commands):
        command = input().split()
        match command[0]:
            case 'pop':
                S.pop()
            case 'remove':
                S.remove(int(command[1]))
            case 'discard':
                S.discard(int(command[1]))
    print(sum(S))
