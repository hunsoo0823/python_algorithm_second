import heapq
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 도시의 갯수 n, 통로의 개수 m, 메시지를 보내는 도시 c
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
# 도시의 모든 거리를 무한으로 초기화
distance = [INF] * (n+1)

# 각 노드에 연결되어 있는 도시의 정보 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접한 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하느 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start = c
# 다익스트라 알고리즘을 수행
dijstra(start)
max_distance = -1
city_count = 0

for i in range(1, n+1):
    if distance[i] != INF:
        city_count += 1
        max_distance = max(max_distance, distance[i])

# 시작노드는 제외해야하므로 count -= 1을출력
print(city_count - 1, max_distance)