# number n
n = int(input())

number_array = []
for i in range(n):
    number_array.append(int(input()))

number_array = sorted(number_array, reverse=True)

print(number_array)