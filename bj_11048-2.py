# Bottom-Up

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []
dp = [[0 for c in range(M)]for r in range(N)]

for i in range(N):
    data.append(list(map(int, input().split())))


dp[0][0] = data[0][0]

for i in range(0, N):
    for j in range(0, M):
        if i+1<N and j+1 <M:
            dp[i+1][j+1] = max(dp[i][j] + data[i+1][j+1], dp[i+1][j+1])
        if i+1<N:
            dp[i+1][j] = max(dp[i][j] +data[i+1][j], dp[i+1][j])
        if j+1<M:
            dp[i][j+1] = max(dp[i][j] + data[i][j+1], dp[i][j+1])

print(dp[N-1][M-1])

