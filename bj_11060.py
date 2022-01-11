import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

dp = [int(1e9)] * N

dp[0] = 0

for i in range(N):
    for c in range(1, data[i]+1):
        if i + c < N:
            dp[i+c] = min(dp[i+c], dp[i]+1)

if dp[N-1] == int(1e9):
    print(-1)
else:
    print(dp[N-1])