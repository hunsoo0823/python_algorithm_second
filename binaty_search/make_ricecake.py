# 떡의 개수 n, 요청한 떡의 길이 m
n, m = map(int, input().split())

ricecake_list = list(map(int, input().split()))

start = 0
end = max(ricecake_list)

result = 0
# 요청한 길이의 떠 자르기
while(start <= end):
    total = 0

    mid = (start + end) // 2
    for ricecake in ricecake_list:
        if ricecake > mid:
            total += ricecake - mid
    
    if total > m:
        start = mid + 1
        result = mid
    elif total < m:
        end = mid - 1
    else:
        result = mid
        break

print(result)


    
        



    
    
