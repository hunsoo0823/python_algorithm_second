dx = [-1, 0, 1]
dy = [1, 1, 1] 

# 테스트 케이스 T 만큼 반복
for _ in range(int(input())):
    n, m = map(int, input().split())

    mine_array = []
    input_array = list(map(int, input().split()))
    dynamic_array = [[0] * m for _ in range(n)]
    
    for i in range(n):
        mine_array.append(input_array[i*m:i*m+m])
        dynamic_array[i][0] = input_array[i*m]

    for i in range(m-1):
        for j in range(n):
            for k in range(3):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx >= 0 and nx < n:
                    dynamic_array[nx][ny] = max(dynamic_array[nx][ny], dynamic_array[j][i] + mine_array[nx][ny])

    print(mine_array)

    max_num = 0
    for i in range(n):
        if max_num < dynamic_array[i][m-1]:
            max_num = dynamic_array[i][m-1]

    print(max_num)
    
