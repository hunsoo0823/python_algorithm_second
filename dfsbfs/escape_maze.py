from collections import deque

# N * M 크기의 미로
n, m = map(int, input().split())

maze_graph = [] 
for _ in range(n):
    maze_graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0 ,1, -1]

def bfs(x, y):
    
    # 큐 생성
    queue = deque()
    # 시작 좌표 입력
    queue.append((x,y))

    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어 난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 괴물이 있는 경우
            if maze_graph[nx][ny] == 0:
                continue
                
            # 처음 방문한경우에만 최단 거리 기록
            if maze_graph[nx][ny] == 1:
                queue.append((nx, ny))
                maze_graph[nx][ny] = maze_graph[x][y] + 1
    
    return maze_graph[n-1][m-1]

distance = bfs(0, 0)
print(distance)

                