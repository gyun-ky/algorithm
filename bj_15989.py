import sys
# input = sys.stdin.readline()

n = int(input())

dp = [1] * 10001

for i in range(2, 4):
    for j in range(1, 10001):
        if j >= i:
            dp[j] += dp[j-i]


        

for i in range(n):
    a = int(input())
    print(dp[a])

