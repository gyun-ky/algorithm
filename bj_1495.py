N, S, M = map(int, input().split())

V = list(map(int, input().split()))
V.insert(0, -1)
print(V)
dp = [[False]*M for i in range(N)]
print(dp)


if 0<= S-V[0] <M:
    dp[0][S-V[0]] = True

if 0<= S+V[0] <M:
    dp[0][S+V[0]] = True

answer = 0
for i in range(1, N):
    for j in range(0, M):
        if 0<= S-V[0] <M and dp[i-1][S+V[0]]:
            dp[i][S-V[0]] = True
            if i== N-1:
                answer = max(answer, j)

        if 0<= S+V[0] <M and dp[i-1][S-V[0]]:
            dp[i][S+V[0]] = True
            if i== N-1:
                answer = max(answer, j)


print(answer)
