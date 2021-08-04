import sys
input = sys.stdin.readline
INF = (1e9)

N, M, C = map(int, input().split())

graph = [[INF]*(N+1) for i in range(0, N+1)]


for _ in range(0, M):
    X, Y, Z = map(int, input().split())
    graph[X][Y] = Z

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

time = 0
cnt = 0

for i in range(1, N+1):
    if graph[C][i] != INF and i != C:
        time = max(time, graph[C][i])
        cnt += 1

print(f'{cnt} {time}')

