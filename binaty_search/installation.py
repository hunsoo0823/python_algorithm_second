# 집의 갯수 n, 설치 공유기 갯수 c
n, c = map(int, input().split())

house_list = []
# 집의 좌표
for i in range(n):
    house_list.append(int(input()))

house_list.sort()

# 가장 작은 차이 start , 가장 큰 차이 end
start = 1
end = house_list[-1] - house_list[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    count = 1
    value = house_list[0]

    for i in range(1, n):
        if house_list[i] >= mid + value:
            count += 1
            value = house_list[i]
    if count >= c:
        start = mid + 1
        result = mid 
    else:
        end = mid - 1

print(result)