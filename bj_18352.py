import heapq
INF = int(1e9)

N, M, K, X = map(int, input().split())

# M - 도로 개수 K 거리 정보, X - 출발 도시 번호

graph = [list() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


visited = [False] * (N+1)
visited[0] = True
dist = [INF] * (N+1)
dist[X] = 0

q = []
heapq.heappush(q, (0, X))

while q:
    d, v = heapq.heappop(q)

    visited[v] = True
    
    for nv in graph[v]:
        if visited[nv] is False and d+1 < dist[nv]:
            dist[nv] = d+1
            heapq.heappush(q, (d+1, nv))

answer_idx = []
for i in range(1, N+1):
    if dist[i] == K:
        answer_idx.append(i)
    
if answer_idx:
    for idx in answer_idx:
        print(idx)
else:
    print(-1)
    




