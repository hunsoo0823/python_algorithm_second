# 문자열 S를 입력받음
str = input()
rearrange_str = []
sum_num = 0

for i in range(len(str)):
    if 65 <= ord(str[i]) <= 90:
        rearrange_str.append(str[i])
    else:
        sum_num += int(str[i])

# 오름차순으로 재정렬
rearrange_str.sort()

for str in rearrange_str:
    print(str, end='')
print(sum_num)