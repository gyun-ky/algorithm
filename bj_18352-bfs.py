from collections import deque
INF = int(1e9)
N, M, K, X = map(int, input().split())

# M - 도로 개수 K 거리 정보, X - 출발 도시 번호

graph = [list() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


dist = [INF] * (N+1)

q = deque()
q.append((X, 0))
visited = [False] * (N+1)
visited[X] = True
dist[X] = 0

while q:
    v, d = q.popleft()

    for nv in graph[v]:
        if visited[nv] is False:
            visited[nv] = True
            dist[nv] = d+1
            q.append((nv, d+1))

answer_idx = []
for i in range(1, N+1):
    if dist[i] == K:
        answer_idx.append(i)
    
if answer_idx:
    for idx in answer_idx:
        print(idx)
else:
    print(-1)
    


