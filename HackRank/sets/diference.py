"""difference"""

if __name__ == '__main__':
    n = int(input())
    eng_students = set(map(int, input().split()))
    b = int(input())
    fre_students = set(map(int, input().split()))
    res = eng_students.difference(fre_students)
    print(len(res))
