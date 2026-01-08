"""Minion Game"""

def minion_game(string: str):
    """Minion Game"""
    vowels = 'AEIOU'
    kevin = stuart = 0

    for i, char in enumerate(string):
        if char in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
