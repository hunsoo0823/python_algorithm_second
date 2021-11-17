# 원소의 갯수 N, 찾는 수 x

N, x = map(int, input().split())

sorted_list = list(map(int, input().split()))
count = 0

def binary_search(array, target, start, end):

    if start > end:
        return 

    global count
    mid = (start + end) // 2
    if array[mid] == target:
        count += 1
        binary_search(array, target, start, mid-1)
        binary_search(array, target, mid+1, end)
    elif array[mid] < target:
        binary_search(array, target, mid+1, end)
    else:
        binary_search(array, target, start, mid-1)

binary_search(sorted_list, x, 0, len(sorted_list)-1)

if count == 0:
    print(-1)
else:
    print(count)