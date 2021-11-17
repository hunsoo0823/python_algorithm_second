# 수열의 갯수 N
n = int(input())

# 수열 입력받기
fixed_list = list(map(int, input().split()))
fixed = -1

def binary_search(array, start, end):
    
    global fixed

    if start > end:
        return

    mid = (start + end) // 2
    
    if array[mid] == mid:
        fixed = mid 
    else:
        if array[mid] <= 0:
            binary_search(array, mid+1, end)
        else:
            binary_search(array, start, mid-1)
            binary_search(array, mid+1, end)
    
binary_search(fixed_list, 0, len(fixed_list)-1)

if fixed == -1:
    print(-1)
else:
    print(fixed)    


    