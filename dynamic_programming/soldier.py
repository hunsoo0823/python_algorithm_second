# 병사의 수 N
n = int(input())

# 전투력 정보의 리스트
soider_array = list(map(int, input().split()))
soider_array.reverse()

d = [1] * (n)
for i in range(1, n):
    for j in range(0, i):
        if soider_array[j] < soider_array[i]:
                d[i] = max(d[i], d[j]+1)
        
print(n - max(d))