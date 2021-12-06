# 삼각형의 크게 n
n = int(input())

triangle_array = []
for i in range(n):
    triangle_array.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(i+1):
        # 가장 왼쪽에 있을때
        if j == 0:
            left_up = 0
        else:
            left_up = triangle_array[i-1][j-1]
        
        # 가장 오른쪽에 있을때
        if j == i:
            right_up = 0
        else:
            right_up = triangle_array[i-1][j]
        
        triangle_array[i][j] = triangle_array[i][j] + max(left_up, right_up)

result = 0
for i in range(n):
    result = max(result, triangle_array[n-1][i])

print(result)