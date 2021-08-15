# n, k 입력받기
n, k = map(int, input().split())

count = 0
while True:
    # n이 1이 되었을 때 종료
    if n == 1:
        break

    # n이 k로 나누어 질때
    if n % k == 0:
        n //= k
    # n이 k로 나누어 지지 않을때,
    else:
        n -= 1

    count += 1

print(count)
    

