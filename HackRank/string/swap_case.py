"""swap_case"""

def swap_case(string: str):
    """swap the case of the string"""
    return ''.join(i.lower() if i.isupper() else i.upper() for i in string)

if __name__ == '__main__':
    s = input()
    RESULT = swap_case(s)
    print(RESULT)
