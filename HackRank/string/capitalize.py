"""capitalize"""

def solve(text: str):
    """capitalize"""
    return ' '.join(word.capitalize() for word in text.split(' '))


if __name__ == '__main__':

    s = input()
    print(solve(s) + '\n')
