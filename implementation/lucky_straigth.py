# n 자리수 정수
lucky_num = input()
n = len(lucky_num)

half = n // 2 # 왼쪽과 오른쪽을 나눌 정수
left_sum = 0 # 왼쪽 수의 합
right_sum = 0 # 오른쪽 수의 합

for i in range(half):
    left_sum += int(lucky_num[i])

for j in range(half, n):
    right_sum += int(lucky_num[j])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")