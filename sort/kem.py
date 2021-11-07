# student number
n = int(input())

kem_grade = []
for _ in range(n):
    name, kor, eng, math = input().split()
    kem_grade.append((name, int(kor), int(eng), int(math)))

kem_grade.sort(key=lambda x: (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))

# print name
for student in kem_grade:
    print(student[0])