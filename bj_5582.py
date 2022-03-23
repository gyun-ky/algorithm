# 두 문자열이 주어졌을 때 
# 모두 포함된 가장 긴 문자열

# dp[i][j] - arr1 을 i번째까지, arr2를 j번째까지 봤을 때, 부분 문자열 중 가장 긴 것

# i번째와 j번째가 같은 경우 
# dp[i][j] = dp[i-1][j-1] + 1

# i번쨰와 j번째가 같지 않은 경우
# max_length 값을 update
# dp[i-1][j] 와 dp[i][j-1] 값 중 큰 것을 max length로 update
# dp[i][j] = 0



# i에서 j까지
