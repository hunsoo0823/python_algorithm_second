INF = 1e9

# 도시의 갯수 n
n = int(input())
# 버스의 갯수 m
m = int(input())

# 도시 그래프 초기화
city_graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n+1):
    city_graph[i][i] = 0

for _ in range(m):
    # a->b 비용 c
    a, b, c = map(int, input().split())
    if city_graph[a][b] > c:
        city_graph[a][b] = c 

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
                city_graph[i][j] = min(city_graph[i][k] + city_graph[k][j], city_graph[i][j])

for i in range(1,n+1):
    for j in range(1, n+1):
        print(city_graph[i][j], end=' ')
    print()