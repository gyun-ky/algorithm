# Bottom-Up (최적화)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []
dp = [[0 for c in range(M)]for r in range(N)]

for i in range(N):
    data.append(list(map(int, input().split())))

dp[0][0] = data[0][0]

for i in range(N):
    for j in range(M):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + data[i][j]

print(dp[N-1][M-1])