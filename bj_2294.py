# n가지 종류의 동전
# 최소로 동전의 개수


n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

# dp[i] 가치의 합이 i일 때, 사용한 동전 최소 개수

# dp[i] = min (dp[i], dp[i-j]+1)

dp = [int(1e9)]*(k+1)
dp[0] = 0

for c in coin:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == int(1e9):
    print(-1)
else:
    print(dp[k])