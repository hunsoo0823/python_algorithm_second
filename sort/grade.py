# student number
n = int(input())

# name , grade
array = []
for i in range(n):
    name, grade = input().split()
    array.append((name, int(grade)))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
print()