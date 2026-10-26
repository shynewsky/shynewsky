students = [i+1 for i in range(30)]
projects = [int(input()) for _ in range(28)]

for student in students:
    if student not in projects:
        print(student)
