# 복도의 크기 N입력
n = int(input())

# 복도의 정보 입력 (n*n)
corridor_graph = []
teacher = []
for i in range(n):
    input_cor = list(input().split())
    corridor_graph.append(input_cor)
    for j in range(n):
        if input_cor[j] == 'T':
            teacher.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bool_avoid = False
bool_observe = True

def observing(dir, x, y):
    global bool_observe
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return 

    if corridor_graph[nx][ny] == 'O':
        return
    if corridor_graph[nx][ny] == 'S':
        bool_observe = False
    else:
        if bool_observe == True:
            observing(dir, nx, ny)
            
def check_avoid():

    global bool_observe
    bool_observe = True
    for i in range(len(teacher)):
        x, y = teacher[i]
        for i in range(4):
            observing(i, x, y)
    
    if bool_observe == True:
        return True
    else:
        return False

def dfs(count):
    global bool_avoid

    if bool_avoid == True:
        return 

    if count == 3:
       if check_avoid() == True:
           bool_avoid = True

    else:
        for i in range(n):
            for j in range(n):
                if corridor_graph[i][j] == 'X':
                    corridor_graph[i][j] = 'O'
                    count += 1
                    dfs(count)
                    corridor_graph[i][j] = 'X'
                    count -= 1    

dfs(0)

if bool_avoid == True:
    print('YES')
else:
    print('NO')