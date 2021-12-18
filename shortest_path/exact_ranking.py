# 학생수 n, 두학생의 성적을 비교한 횟수 m
n, m = map(int, input().split())

INF = 1e9

graph_ranking = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph_ranking[i][i] = 0

for i in range(m):
    # a -> b (a가 b보다 성적이 낮다)
    a, b = map(int ,input().split())
    graph_ranking[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph_ranking[a][b] = min(graph_ranking[a][k] + graph_ranking[k][b], graph_ranking[a][b])

count = 0

for i in range(1, n+1):
    check_rank = 0
    for j in range(1, n+1):
        if graph_ranking[i][j] == INF and graph_ranking[j][i] == INF:
            break
        check_rank += 1
    if check_rank == n:
        count += 1
    
print(count)