# 문자열 S입력 받기
s = input()

# 모든 숫자를 1 혹은 0으로 바꾸는 데 필요한 횟수
count_one = 0
count_zero = 0

# 그 전의 수를 담는 변수
before = s[0]

for i in range(1, len(s)):
    if before == '0':
        # 0이 이어지는 경우
        if s[i] == before:
            continue
        # 다음 숫자가 1인 경우
        else:
            count_one += 1 # 0 -> 1 변환
            before = s[i] # 1

    else: # before == 1
        # 1이 이어지는 경우
        if s[i] == before:
            continue
        else:
            count_zero += 1 # 1 -> 0 변환
            before = s[i] # 0

# 마지막 숫자 count
if before == '0':
    count_one += 1
else:
    count_zero += 1

print(count_one, count_zero)