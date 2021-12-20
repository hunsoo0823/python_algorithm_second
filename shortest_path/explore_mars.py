import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = 1e9

# 테스크 케이스 수 입력
for i in range(int(input())):
    # 탐사 공간의 크기 n
    n = int(input())

    # mars graph
    mars_graph = []
    for _ in range(n):
        mars_graph.append(list(map(int, input().split())))
    # 지도 그래프 초기화
    path_graph = [[INF] * n for _ in range(n)]
    path_graph[0][0] = mars_graph[0][0]
    # 좌표를 넣을 큐
    q = []
    # 시작 좌표 큐에 입력
    # distance, 0, 0
    heapq.heappush(q, (mars_graph[0][0],0,0))
    
    while q:
        dist, x, y = heapq.heappop(q)

        # 동서남북 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 초과시 처리 안함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            cost = dist + mars_graph[nx][ny]
            
            if cost < path_graph[nx][ny]:
                path_graph[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
                
    print(path_graph[n-1][n-1])
            
                

    
    
    