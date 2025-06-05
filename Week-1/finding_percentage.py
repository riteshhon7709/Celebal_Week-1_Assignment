n = int(input())
student_marks = {}

for _ in range(n):
    name, *marks = input().split()
    student_marks[name] = list(map(float, marks))

query_name = input()
avg = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{avg:.2f}")
