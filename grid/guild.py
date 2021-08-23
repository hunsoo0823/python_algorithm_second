# n명의 모험가
n = int(input())

# 각 모험가의 공포도 
adventure = list(map(int, input().split()))

# 공포도를 오름차순으로 정렬
adventure.sort()
# 각 소그룹의 맴버
fear = []
count = 0

for adv in adventure:
    # 소그룹에 포함 시키기
    fear.append(adv)
    # 소그룹의 가장 큰 공포도
    max_fear = max(fear)
    # 공포도보다 인원수가 많을때, 그룹 결정 짓기
    if max_fear <= len(fear):
        fear = []
        count += 1

print(count)
