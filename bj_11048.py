import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = []
dp = [[0 for c in range(M)]for r in range(N)]
for i in range(N):
    data.append(list(map(int, input().split())))

tmp_sum1 = 0
for j in range(M):
    tmp_sum1 += data[0][j]
    dp[0][j] = tmp_sum1

tmp_sum2 = 0
for i in range(N):
    tmp_sum2 += data[i][0]
    dp[i][0] = tmp_sum2

for i in range(1, N):
    for j in range(1, M):
        max_num = max(dp[i-1][j] + data[i][j], dp[i][j-1]+data[i][j])
        max_num_result = max(max_num, dp[i-1][j-1]+data[i][j])
        dp[i][j] = max_num_result


print(dp[N-1][M-1])