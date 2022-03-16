N = int(input())

dp = [0] * (N+1)
dp[1] = 1

for i in range(2, N+1):
    max_cnt = i # A만 계속 쭉 눌렀을 때
    max_cnt = max(max_cnt, dp[i-1]+1) # 방법 1 ) A를 한번 눌렀을 때
    for k in range(1, i):
        max_cnt = max(max_cnt, dp[i-(k+2)]*(k+1))

    dp[i] = max_cnt



print(dp[N])
