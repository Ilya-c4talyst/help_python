students_count = int(input())

first_sem = set(map(str, input().split()))

second_sem = set(map(str, input().split()))

cool_students = first_sem.intersection(second_sem)

if len(cool_students) == 0:
    print('No students participated in both seminars')
else:
    print(' '.join(sorted(cool_students)))

bad_students_count = students_count - len(first_sem.union(second_sem))

print(bad_students_count)
