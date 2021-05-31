n = int(input())
k = int(input())

dp = [[0 for j in range(0, k+1)] for i in range(0, n+1)]
 

def b_coef(n, k):
    
    for i in range(0, n+1):
        for j in range(0, min(i, k)+1):
            if j==0 or j==i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n][k]

print(b_coef(n, k))
print(dp)

