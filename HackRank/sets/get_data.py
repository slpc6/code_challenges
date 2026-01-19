""""data for some files"""

def inputs():
    """return the data for some files"""
    n = int(input())
    eng_students = set(map(int, input().split()))
    b = int(input())
    fre_students = set(map(int, input().split()))
    print(n, b)
    return eng_students, fre_students
