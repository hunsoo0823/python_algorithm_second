# 식량 창고의 개수 N
n = int(input())

# 식량 창고에 저장된 식량의 갯수
k = list(map(int, input().split()))

d = [0] * n
d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2,n):
    d[i] = max(d[i-2]+k[i], d[i-1])

print(d[n-1])