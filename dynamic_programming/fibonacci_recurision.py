d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2 일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적이 있는 문제라면 그래도 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
    