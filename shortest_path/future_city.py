INF = 1e9

# 전체 회사의 개수 N, 경로 M
n, m = map(int, input().split())

# 전체 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b  = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x번회사, 소개팅장소 k번 회사
x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달 할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할 수 없다면, 최단 거리를 출력
else:
    print(distance)