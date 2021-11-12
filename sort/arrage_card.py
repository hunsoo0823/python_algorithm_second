import heapq

n = int(input())


card_heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(card_heap, data)

result = 0

while len(card_heap) != 1:
    # 가장 작은 2개의 카드의 묶음 꺼내기
    one = heapq.heappop(card_heap)
    two = heapq.heappop(card_heap)
    
    sum_value = one + two
    result += sum_value
    heapq.heappush(card_heap, sum_value)

print(result)

print(result)
