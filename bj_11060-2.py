import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

dp = [int(1e9)] * N

dp[0] = 0

for i in range(1, N):
    for j in range(0, i):
        if dp[j] != int(1e9) and i-j <= data[j] :
        # dp에 값이 있어야하고 두칸 사이의 거리가 data[j] 보다 같거나 작아야함
            if dp[i] > dp[j] + 1:
                dp[i] = dp[j] + 1


if dp[N-1] == int(1e9):
    print(-1)
else:
    print(dp[N-1])