"""find_string"""
def count_substring(string: str, sub_string: str) -> int:
    """count the number of times a substring appears in a string"""
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))

if __name__ == '__main__':
    s = input().strip()
    sub_s = input().strip()
    count = count_substring(s, sub_s)
    print(count)
