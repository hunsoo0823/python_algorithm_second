from itertools import permutations

n = 12
weak = [1,5,6,12]
dist = [1,2,3,4]

# 외벽의 길이 n, 취약점의 위치가 담긴 배열 week, 1시간동안 이동할 수 있는 거리 배열 dist
def solution(n, weak, dist):
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입 요원 수
            position = weak[start] + friends[count-1]
            
            for index in range(start, start+length):
                # 점거가능 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 요원 하나 더 투입
                    if count > len(dist): # 더 투입할 요원이 없는 경우
                        break
                    position = weak[index] + friends[count - 1]

            answer = min(answer, count)      

    if answer == len(dist) + 1: # 요원을 모두 투입해도 취약 지점을 점검할 수없는 경우
        return -1
    return answer

answer = solution(n, weak, dist)
print(answer)