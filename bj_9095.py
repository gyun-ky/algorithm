import sys

n = int(input())

dp = [0] * 10001
dp[0] = 1

for i in range(1, 10001):
    for j in range(1, 4):
        if i-j >= 0:
            dp[i] += dp[i-j]


        

for i in range(n):
    a = int(input())
    print(dp[a])

