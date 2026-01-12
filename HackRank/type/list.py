""""lists"""

if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        S = input().split()
        match S[0]:
            case 'insert':
                ls.insert(int(S[1]), int(S[2]))
            case 'print':
                print(ls)
            case 'remove':
                ls.remove(int(S[1]))
            case 'append':
                ls.append(int(S[1]))
            case 'sort':
                ls.sort()
            case 'pop':
                ls.pop()
            case 'reverse':
                ls.reverse()
