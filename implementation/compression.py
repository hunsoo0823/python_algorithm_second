# 문자열 입력받기
original_str = input()
min_len = 1001

if len(original_str) == 1:
    min_len = 1
       
for i in range(1, len(original_str)//2+1):
    
    count = 1 # 몇개가 압축됬는지 확인할 변수
    before_alp = original_str[0:i]
    com_str = ""

    for j in range(1, len(original_str) // i + 1):
        if before_alp == original_str[i*j:i*(j+1)]:
            count += 1
        else:
            if count == 1:
                com_str += before_alp
                before_alp = original_str[i*j:i*(j+1)]
            else:
                com_str += str(count)
                com_str += before_alp
                before_alp = original_str[i*j:i*(j+1)]
                count = 1
    
    com_str += original_str[i*j:]
    
    if len(com_str) < min_len:
        min_len = len(com_str)
    print(len(com_str))
    print(i, com_str)
    
print(min_len)