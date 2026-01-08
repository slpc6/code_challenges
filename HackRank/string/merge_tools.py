"""merge_the_tools"""

def merge_the_tools(string: str, k: int):
    """merge_the_tools"""
    parts = [string[i: i+k] for i in range(0, len(string), k)]
    parts = [''.join(dict.fromkeys(part)) for part in parts]
    print(*(part for part in parts), sep='\n')
if __name__ == '__main__':
    text, n = input(), int(input())
    merge_the_tools(text, n)
