# house number n
n = int(input())

# location of house
house_array = list(map(int, input().split()))

house_array.sort()
print(house_array[(n-1)//2])
    

"""
min_distance = 1e9
min_index = 0
for i in range(1, (max(house_array)+1)):
    distance = 0
    for hosuse in house_array:
        distance += abs(i-hosuse)
    if distance < min_distance:
        min_distance = distance
        min_index = i

"""

