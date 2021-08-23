# 동전의 개수 N
n = int(input())

# 화폐의 단위 
coin_array = list(map(int, input().split()))
coin_array.sort()

target = 1

for x in coin_array:
    print(x)
    # 만들 수 없는 금액일 때 반복 종료
    if target < x:
        break
    target += x

print(target)
    
