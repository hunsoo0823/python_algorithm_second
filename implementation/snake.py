from collections import deque
import queue

# 보드의 크기 N
n = int(input())

# 사과의 갯수 K
k = int(input())

# 사과의 위치 입력받기
apple_map = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    # 좌표 (x,y)의 위치에 1
    apple_map[x-1][y-1] = 1

snake_dir = deque()
snake = deque()
direction = 0 # R 시작방향 오른쪽

# 뱀의 방향 전환 횟수
l = int(input())

# 뱀의 방향에 관한 정보 
for _ in range(l):
    a, b = input().split()
    snake_dir.append((int(a), b))

# R, D, L, U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 1
snake.append((0,0))
time, dir = snake_dir.popleft()

def turn(d):
    global direction
    if d == 'L':
        direction -= 1
        if direction < 0:
            direction = 3
    else:
        direction += 1
        if direction > 3:
            direction = 0

while True:     

    # 뱀의 머리 좌표
    x, y = snake.popleft()
    
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 범위를 벗어났을때 게임 종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break
    elif (nx,ny) in snake: # 자기 자신과 부딪혔을때
        break
    else:
        if apple_map[nx][ny] == 1: # 사과를 발견했을때,
            snake.appendleft((nx,ny))
            snake.append((x,y))
        else:
            snake.appendleft((nx,ny))
    
    if count == time:
        turn(dir)
        time, dir = snake_dir.pop()

    print(snake)
    count += 1


print(count)
    



        
    
    
