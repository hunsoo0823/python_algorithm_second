# 세로 크기 N, 가로크기 M 
n, m = map(int, input().split())
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤 맵 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

lab_graph = []
for i in range(n):
    lab_graph.append(list(map(int, input().split())))

result = 0

def get_socre():
    score = 0
    for i in range(n):
        for j in range(m):
            # 바이러스가 퍼져있지 않은 영역 socre 추가
            if temp[i][j] == 0:
                score += 1
        
    return score

def virus(x, y):
    
    # 동서남북 바이러스 전파
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위를 벗어나는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 바이러스가 벽아나 바이러스를 만난경우
        if temp[nx][ny] == 1 or temp[nx][ny] == 2:
            continue
        
        # 바이러스가 전파가 가능한 경우
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab_graph[i][j]
    
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전영역 최댓 값 계산
        result = max(get_socre(), result)       
        return 

    for i in range(n):
        for j in range(m):
            if lab_graph[i][j] == 0:
                lab_graph[i][j] = 1
                count += 1
                dfs(count)
                lab_graph[i][j] = 0
                count -= 1

dfs(0)
print(result)


        

        

