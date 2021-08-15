# n명의 모험가
n = int(input())

# 각 모험가의 공포도 
adventure = list(map(int, input().split()))

# 공포도를 오름차순으로 정렬
adventure.sort()
# 각 그룹의 맴버
fear = []
count = 0

for adv in adventure:
    fear.append(adv)
    max_fear = max(fear)
    if max_fear <= len(fear):
        fear = []
        count += 1

print(count)
