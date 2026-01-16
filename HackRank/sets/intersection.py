"""intersection"""

if __name__ == '__main__':
    n = int(input())
    eng_students = set(map(int, input().split()))
    b = int(input())
    fre_students = set(map(int, input().split()))
    unique = eng_students.intersection(fre_students)
    print(len(unique))
