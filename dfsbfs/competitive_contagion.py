# N * N 크기의 시험관, k개의 바이러스 종류
from collections import deque

n, k = map(int, input().split())
ex_list = []
examiner_graph = []

for i in range(n):
    input_ex = list(map(int, input().split()))
    examiner_graph.append(input_ex)
    for j in range(n):
        if input_ex[j] != 0:
            ex_list.append((input_ex[j], 0, i, j))

ex_list.sort()
queue = deque(ex_list)

# s 초, x,y 좌표 입력
s, t_x, t_y = map(int, input().split())

# 바이러스 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    virus, time , x, y = queue.popleft()
    # 정확히 s초가 지나거나, 큐가 빌때까지 반복
    if time == s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 없는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문 하지 않은 위치라면, 그 위치에 바이러스 삽입
            if examiner_graph[nx][ny] == 0:
                examiner_graph[nx][ny] = virus
                queue.append((virus, time+1, nx, ny))

print(examiner_graph[t_x-1][t_y-1])
