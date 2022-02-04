N, S, M = map(int, input().split())

V = list(map(int, input().split()))
V.insert(0, -1)
dp = [[False]*(M+1) for i in range(N+1)]


dp[0][S] = True

answer = -1
for i in range(N):
    for j in range(M+1):
        if dp[i][j] is False:
            continue
    
        if 0<= j+V[i+1] <= M :
            dp[i+1][j+V[i+1]] = True
            if i == N-1:
                answer = max(answer, j+V[i+1])

        if 0<= j-V[i+1] <= M :
            dp[i+1][j-V[i+1]] = True
            if i == N-1:
                answer = max(answer, j-V[i+1])
        


print(answer)