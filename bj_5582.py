

a = list(input())
b = list(input())

a.insert(0, '0')
b.insert(0, '0')


dp = [[0]*len(b) for _ in range(len(a))]

answer = 0

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
        else:
            dp[i][j] = 0

print(answer)