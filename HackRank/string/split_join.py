"""split_join"""

def split_and_join(line: str):
    """split the string and join it with a hyphen"""
    return '-'.join(line.split())

if __name__ == '__main__':
    l = input()
    RESULT = split_and_join(l)
    print(RESULT)
