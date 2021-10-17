import itertools

INF = 1e9
# 크기 n, 치킨집의 갯수 m
n, m = map(int, input().split())

chicken = []
home = []
city_graph = []
# 도시의 정보
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n): 
        if city[j] == 2: # 치킨집의 좌표 저장
            chicken.append((i, j))
        if city[j] == 1:
            home.append((i,j)) # 집의 좌표 저장
    city_graph.append(city)

nCr = list(itertools.combinations(chicken, m))


min_chicken_dis = INF
for C in nCr:
    chicken_dis = 0
    for h in home:
        min_dis = INF
        for c in C:
            dis = abs(h[0]-c[0]) + abs(h[1]-c[1])
            if min_dis > dis:
                min_dis = dis
        chicken_dis += min_dis
    if min_chicken_dis > chicken_dis:
        min_chicken_dis = chicken_dis

print(min_chicken_dis)


"""
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
""