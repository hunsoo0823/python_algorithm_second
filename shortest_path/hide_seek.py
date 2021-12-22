import heapq
import sys
input = sys.stdin.readline
INF = 1e9

# n개의 헛간, m개의 양뱡향 통로
n, m = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
hide_graph = [[] * (n+1) for _ in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    # a 헛간에서 b 헛간까지 양방향 연결
    a, b = map(int, input().split())
    hide_graph[a].append((b, 1))
    hide_graph[b].append((a, 1))

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # q가 빌때 까지 반복
    while q:
        print(q)
        dist, now = heapq.heappop(q)

        # 이미 처리된적이 있는 노드라면 무시
        if dist > distance[now]:
            continue
        
        # 그래프에 연결된 간선 확인
        for i in hide_graph[now]:
            cost = dist + i[1]

            # 다른 노드를 거쳐가지는 것보다 짧은 경우라면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                 
start = 1
dijstra(start)

max_distance = 0
max_node = 0
same_distance_node = 0

for i in range(1,n+1):
    if max_distance < distance[i]:
        max_distance = distance[i]
        max_node = i

for i in range(1, n+1):
    if distance[i] == max_distance:
        same_distance_node += 1

print(max_node, max_distance, same_distance_node)

    