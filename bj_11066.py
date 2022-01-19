
T = int(input())

for _ in range(T):

    N = int(input())


    data= list(map(int, input().split()))

    dp = [[int(1e9) for i in range(N)] for j in range(N)]
    sum_arr = [[0 for i in range(N)] for j in range(N)]

    for diag in range(N):
        i=0
        for j in range(diag, N):
            if i==j :
                sum_arr[i][j] = data[i]
            else:
                sum_arr[i][j] = sum_arr[i][j-1] + data[j]
            i+=1

    for diag in range(N):
        i = 0
        for j in range(diag, N):
            print(f'{i} {j}')
            if i==j :
                dp[i][j] = 0
            else:
                for k in range(i, j):
                    tmp = dp[i][k] + dp[k+1][j] + sum_arr[i][j]
                    dp[i][j] = min(tmp, dp[i][j])
            i+=1

    print(dp[0][N-1])