"""split_join"""

def split_and_join(line):
    """split the string and join it with a hyphen"""
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
