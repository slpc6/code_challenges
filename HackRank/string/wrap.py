"""wrap a text"""
import textwrap

def wrap(string: str, max_width: int):
    """wrap a text"""
    return ''.join(i+ '\n' for i in textwrap.wrap(string, max_width))

if __name__ == '__main__':
    s, max_w = input(), int(input())
    RESULT = wrap(s, max_w)
    print(RESULT)
