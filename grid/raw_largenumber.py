# n, m, k를 공백을 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 수를 공백을 구분하여 입력받기
data = list(map(int, input().split()))

# 데이터를 내림 차순으로 정렬
data.sort(reverse=True)

first = data[0] # 가장 큰수
second = data[1] # 두번째로 큰수

result = 0

for i in range(m):
    if i % (k+1) == 0:
        result += second
    else:
        result += first

print(result)
