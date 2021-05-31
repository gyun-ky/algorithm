n = int(input())
k = int(input())

dp = [[0 for j in range(0, k+1)] for i in range(0, n+1)]

print(dp)
 

def b_coef(n, k):
    
    for i in range(0, n+1):
        for j in range(0, min(i, k)):
            if k==0 or n==k:
                dp[n][k] = 1
            else:
                dp[i][j] = dp[i-1][k-1] + dp[i-1][k]
    return dp[n][k]