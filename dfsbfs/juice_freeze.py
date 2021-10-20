# 얼음틀의 세로길이 N, 가로길이 M
n, m = map(int , input().split())

ice_graph = []
# 얼음 틀의 형태 입력
for i in range(n):
    ice_graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어났을 경우
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 얼음틀에 얼음을 생성할 수 있는 경우
    if ice_graph[x][y] == 0:
        ice_graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True

    return False

# 얼음 계수 
count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)
