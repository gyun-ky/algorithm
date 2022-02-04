N, S, M = map(int, input().split())

V = list(map(int, input().split()))

dp = [[False]*(M+1) for i in range(N)]

answer = -1

if 0<= S-V[0] <=M:
    dp[0][S-V[0]] = True
    if N-1 == 0:
        answer = max(answer, S-V[0])

if 0<= S+V[0] <=M:
    dp[0][S+V[0]] = True
    if N-1 == 0:
        answer = max(answer, S+V[0])


for i in range(1, N):
    for j in range(0, M+1):
        
        if 0<= j-V[i] <=M and dp[i-1][j-V[i]]:
            dp[i][j] = True
            if i== N-1:
                answer = max(answer, j)

        if 0<= j+V[i] <=M and dp[i-1][j+V[i]]:
            dp[i][j] = True
            if i== N-1:
                answer = max(answer, j)

print(answer)