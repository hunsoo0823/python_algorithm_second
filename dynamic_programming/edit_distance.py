def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]

    # dp 테이블 초기화 설정
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 삽입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

    return dp[n][m]

# 문자열 a 입력받기
str_a = input()

# 문자열 b 입력받기
str_b = input()

print(edit_dist(str_a, str_b))