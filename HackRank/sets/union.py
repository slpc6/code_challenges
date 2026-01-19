"""Union"""


from sets.get_data import inputs


if __name__ == '__main__':
    eng_students, fre_students = inputs()
    print(len(eng_students.union(fre_students)))
