# 현재 나이트의 위치 입력받기
input_data = input()
# a1 a->열, 1->행
# row 행(가로), coulmns 열(세로)
row = int(input_data[1])
columns = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

# 이동할 수 있는 경우의 수가 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = columns + step[1]
    
    # 범위를 벗어나지 않는지 확인
    if next_row >= 1 and next_row < 9 and next_col >= 1 and next_col < 9:
        result += 1

print(result)

    

