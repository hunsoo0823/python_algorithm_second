# 볼링공의 갯수 N, 볼링공의 최대 무게 M
n, m = map(int, input().split())

ball = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        if ball[i] != ball[j]:
            count += 1

print(count)
