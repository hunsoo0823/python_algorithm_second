from collections import deque

# map size n, l<N<r
n, l, r = map(int, input().split())

population_graph = []
# input population each map
for _ in range(n):
    population_graph.append(list(map(int, input().split())))

united = deque()

# moving map
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, index):
    united.append((x,y))

    # declare queue for union check
    queue = deque()
    queue.append((x,y))
    union[x][y] = index
    summary = population_graph[x][y]
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                difference = abs(population_graph[x][y] - population_graph[nx][ny])
                
                if difference >= l and difference <= r:
                    queue.append((nx,ny))
                    united.append((nx,ny))
                    union[nx][ny] = index
                    summary += population_graph[nx][ny]
                    count += 1
    
    avg = summary // count 
    while united:
        a, b = united.popleft()
        population_graph[a][b] = avg
    return

# check moving count
totalcount = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            # if i,j is not visted
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1
    
    # if moving is done == union is not maked
    if index == n * n:
        break
    totalcount += 1

print(totalcount)