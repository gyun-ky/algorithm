N, S, M = map(int, input().split())

V = list(map(int, input().split()))
V.insert(0, -1)
print(V)
dp = [[0]*(N+1) for i in range(2)]
print(dp)

dp[0][0] = S
dp[1][0] = S

for j in range(1, N+1):

    if dp[0][j-1] == -1:
        a = -1
    else:
        a = dp[0][j-1] - V[j]
        if a < 0 or a > M:
            a = -1
    
    if dp[1][j-1] == -1:
        b = -1
    else:
        b = dp[1][j-1] - V[j]
        if b < 0 or b > M:
            b = -1
    
    dp[0][j] = max(a, b)
    
    if dp[0][j-1] == -1 :
        c = -1
    else:
        c = dp[0][j-1] + V[j]
        if c < 0 or c > M:
            c = -1

    if dp[1][j-1] == -1:
        d = -1
    else: 
        d = dp[1][j-1] + V[j]
        if d < 0 or d > M:
            d = -1
    
    dp[1][j] = max(c, d)
    
for i in range(2):
    print(dp[i])

print(max(dp[1][N], dp[0][N]))


