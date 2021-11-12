# runtime error

N = 4
stages = [4,4,4,4,4]

def solution(N, stages):
    
    failure_count = []

    n = len(stages)
    for i in range(1,N+1):
        count = stages.count(i)
        if n == 0:
            fail = 0
        else:
            fail = count / n

        failure_count.append((fail, i))
        n -= count
    
    failure_count = sorted(failure_count, key= lambda x: (x[0]), reverse=True)
        
    answer = [i[1] for i in failure_count] 
    return answer      
    
result = solution(N, stages)
print(result)