"""validator"""	

if __name__ == '__main__':
    s = input()
    res = [False] * 5

    for char in s:
        if not res[0] and char.isalnum():
            res[0] = True
        if not res[1] and char.isalpha():
            res[1] = True
        if not res[2] and char.isdigit():
            res[2] = True
        if not res[3] and char.islower():
            res[3] = True
        if not res[4] and char.isupper():
            res[4] = True

        if all(res):
            break
    print(*res, sep='\n')
