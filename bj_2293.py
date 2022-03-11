# n가지 종류의 동전
# 모두 다른 가치
# 가치의 합이 k원 되게 하기 -> 경우의 수
# 동전 구성 같은데 순서만 다르면 같은거

n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

# dp[i] - 합이 i 일때의 경우의 수


# dp = [0] * (k+1)
# dp[0] = 1

# for i in range(1, k+1):
#     for c in coin:
#         if i - c >= 0:
#             dp[i] += dp[i-c]


# print(dp)
# print(dp[k])

dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] += dp[i-c]


# print(dp)
print(dp[k])

