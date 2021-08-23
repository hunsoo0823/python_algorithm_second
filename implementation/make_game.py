# 맵의 세로크기 n, 가로 크기 m
n, m = map(int, input().split())

# 캐릭터 위치 (A, B), 바라보는 방향 d
# 0 : 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
x, y ,direction = map(int, input().split())

move_graph = [[0] * m for _ in range(n)]
move_graph[x][y] = 1

# 맵 입력받기
map_graph = []
for i in range(n):
    map_graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def turn_left():
    global direction
    direction += 1
    if direction > 3:
        direction = 0
    
move_count = 1 # 방문한 칸의 수 확인
turn_count = 0 # 회전한 횟수 확인


while True:
    # 다음에 진행할 방향으로 회전
    turn_left()
    
    # 회전 후 회전 방향으로 이동
    nx = x + dx[direction]
    ny = y + dy[direction]
    turn_count += 1 # 회전 횟수 1 증가

    if map_graph[nx][ny] == 0 and move_graph[nx][ny] == 0: # 육지이거나 가보지 않은 칸 일때
        x, y = nx, ny
        turn_count = 0
        move_count += 1
        move_graph[nx][ny] = 1

    # 회전을 4번 다 수행한경우
    elif turn_count == 4:
        # 뒤로 한칸 이동
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map_graph[nx][ny] == 0: # 육지인 경우
            x, y = nx, ny
            turn_count = 0
        else:
            break

print(move_count)
        

            



