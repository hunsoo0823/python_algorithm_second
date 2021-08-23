def solution(food_times, k):    
    n = len(food_times) # 배열의 크기
    time = 0 # 시간
    count = 0 # 모든 음식을 섭취 했는지 확인할 변수
    answer = 0 # 섭취해야 할 음식의 번호
    
    while True:
        if food_times[answer] != 0:
            food_times[answer] -= 1 # 음식 섭취
            time += 1 # 시간 증가
            count = 0
            
        
        answer += 1
        count += 1
        if answer >= n: # 섭취 음식 번호가 끝자자로 넘어 갔을 떄,
            answer = 0
        
        # 한바퀴를 다 돌았을 때, 더이상 먹을 수 있는 음식이 없음을 의미
        if n < count:
            return -1
        
        if time == k:
            return answer + 1
        
# 먹어야할 n개의 음식, k초의 방송이 중단된 시간
n, k = map(int, input().split())

# 각 음식 섭취에 필요한 시간
food_time = list(map(int, input().split()))

result = solution(food_time, k)

print(result)