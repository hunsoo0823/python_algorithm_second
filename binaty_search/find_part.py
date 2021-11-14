# 매장 부품의 갯수 n
n = int(input())
shop_list = list(map(int, input().split()))
shop_list.sort()

# 손님이 문의하는 부품의 갯수 m
m = int(input())
custom_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for custom in custom_list:
    if binary_search(shop_list, custom, 0, len(shop_list)-1) == True:
        print('yes', end=' ')
    else:
        print('no', end=' ')
    
