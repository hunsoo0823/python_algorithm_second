from collections import deque

# 도시의 개수 n, 도로의 개수 m, 거리 k, 출발 도시 x
n, m, k, x = map(int, input().split())

city_graph = [[] for _ in range(m+1)] 
visted = [False] * (n+1)
distance = [0] * (n+1)

for _ in range(m):
    # a -> b 도시연결
    a, b = map(int ,input().split())
    city_graph[a].append(b)

def bfs(visted, x, graph):
    # 큐에 출발 좌표 입력
    queue = deque([x])
    
    # 출발 좌표 방문 처리
    visted[x] = True

    # 큐가 빌떄까지 반복
    while queue:
        city = queue.popleft()
        for c in graph[city]:
            if not visted[c]:
                visted[c] = True
                distance[c] = distance[city] + 1
                queue.append(c)
        
bfs(visted, x, city_graph)
for i in range(1,n+1):
    if distance[i] == k:
        print(i)                




"""
4 4 2 1
1 2
1 3
2 3
2 4
"""