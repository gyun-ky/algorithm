n = int(input())

dp = [0] * 1000

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] =2*dp[i-2] + dp[i-1]

print(dp[n]%796769)
