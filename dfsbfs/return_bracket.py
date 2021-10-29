# 문자열 입력받기
bracket_input = input()

result = []


def solution(bracket):
    bool_proper = True
    result = ""
    string_u = ""
    string_v = ""
    left_count = 0
    right_count = 0
    if len(bracket) == 0:
        return bracket
    
    for b in bracket:
        if left_count != right_count or (left_count == 0 and right_count == 0):
            if b == '(':
                left_count += 1
                string_u += b
            elif b == ')':
                right_count += 1
                string_u += b

            if left_count < right_count:
                bool_proper = False
        else:
            string_v += b
        
    if bool_proper == False:
        result += '('
        result += solution(string_v)
        result += ')'

        for i in range(1, len(string_u)-1):
            if string_u[i] == '(':
                result += ')'
            else:
                result += '('
    else:
        result += string_u
        result += solution(string_v)

    return result
            
string_r = solution(bracket_input)
print(string_r)

              
