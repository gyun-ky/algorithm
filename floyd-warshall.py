INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for i in range(0, n+1)]

for i in range(0, m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for a in range(1, n+1):
    graph[a][a] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()