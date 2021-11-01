# 수의 개수 n
n = int(input())

# A1,A2 ... An의 수가 주어짐
number_list= list(map(int, input().split()))

# 합이 N-1인 4개의 정수 (+, -, x , /)
plus, minus, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global plus, minus, mul, div, min_value, max_value
    
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + number_list[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - number_list[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * number_list[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / number_list[i]))
            div += 1
    
dfs(1, number_list[0])

print(max_value, min_value)
    