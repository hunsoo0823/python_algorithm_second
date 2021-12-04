# n가지 종류의 화폐 , 가치의 합 m
n, m = map(int, input().split())

INF = 10001

# n개의 줄의 화폐의 가치
money_array = []
for i in range(n):
    money_array.append(int(input()))

d = [INF] * (m+1)
d[0] = 0

for i in range(n):
    for j in range(money_array[i], m+1):
        if d[j - money_array[i]] != INF:
            d[j] = min(d[j - money_array[i]]+1, d[j])

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])