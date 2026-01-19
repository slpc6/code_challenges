""""find the percentage"""


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    val_sum = sum(student_marks[query_name])
    val_count = len(student_marks[query_name])
    total = val_sum/val_count
    print(f"{total:.2f}")
