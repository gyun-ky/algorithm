

def recur(i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    
    result = dp[i][j]
    for k in range(i, j):
        tmp = recur(i, k) + recur(k+1, j) + sum(data[i:j+1])
        if result == -1 or tmp < result:
            result = tmp
            dp[i][j] = result
    

    return result



T = int(input())
for _ in range(T):
    n= int(input())
    data = list(map(int, input().split()))
    dp = [[-1 for i in range(n)] for j in range(n)]
    print(recur(0, n-1))


