# n * m 의 배열
n, m = map(int, input().split())

result = -1

card_graph = []
for _ in range(n):
    card = list(map(int, input().split()))
    min_value = min(card)
    if min_value > result:
        result = min_value

print(result)