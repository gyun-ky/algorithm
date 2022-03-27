# 음수는 가면 안되고
# 20이 넘으면 안된다
# # 0이상 20이하

n = int(input())

data = list(map(int, input().split()))


dp = [[0]*21 for _ in range(n)]

result = data[-1]
data = data[0:-1]

# dp[i][j] i까지 갔을 때, 결과가 j가 되는 개수


# dp[i-1][0] ~ dp[i-1][20] 까지 훑어봤을 때, -1 아닌 것에다가  j 에다가 data[i] 더한거나 뺀 것이 0~20인 경우 dp[i-1][j] + 1 아니면 -1



dp[0][data[0]] = 1

for i in range(1, n-1):
    for j in range(0, 21):

        if dp[i-1][j] != 0:
            if 0 <= j + data[i] <= 20:
                dp[i][j+data[i]] += dp[i-1][j]
            if 0 <= j - data[i] <= 20:
                dp[i][j-data[i]] += dp[i-1][j] 

print(dp[n-2][result])


