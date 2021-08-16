# 숫자 문자열 입력받기
number = input()

result = 0

for i in range(len(number)):
    # 형 변환
    num = int(number[i])
    # 처음에는 0아닌 수를 덧셈을 해야 한다.
    if result == 0:
        if num != 0:
            result += num
    else:
        # 수가 0이나 1일때는 덧셈
        if num == 0 or num == 1:
            result += num
        # 그 외의 경우에는 곱셈
        else:
            result *= num

print(result)