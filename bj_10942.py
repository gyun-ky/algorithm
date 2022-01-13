N = int(input())

data = list(map(int, input().split()))

data.insert(0, 0)

M = int(input())

dp=[[0 for i in range(N+1)]for j in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = data[i]
    if i<N:
        if data[i] == data[i+1]:
            dp[i][i+1] = data[i]

for j in range(3, N+1):
    i = 1
    while i<=N and j<=N:
        if i+1 <= N and j-1 >= 1:
            if dp[i+1][j-1] != 0 and data[i] == data[j]:
                dp[i][j] = data[i]

            j+=1
            i+=1

for q in range(M):
    a, b = map(int, input().split())
    if dp[a][b] == 0:
        print(0)
    else:
        print(1)

