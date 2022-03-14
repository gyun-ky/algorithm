import heapq
INF = int(1e9)

n, e = map(int, input().split())

start = int(input())

# 어떻게 보면 양방향 그래프라고 할수 있을까?
graph = [[] for _ in range(n+1)]

# graph - 양방향 그래프
# 1 -> 2인 경우) graph[1] 에 2가 있고, graph[2] 에 1이 있다
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [False] * (n+1)
visited[0] = True

dist = [int(1e9)] * (n+1)
dist[start] = 0

q = []
heapq.heappush(q, (0, start))
visited[start] = True

while True:

    if len(q) == 0:
        break

    distance, vertex = heapq.heappop(q)

    for adj_node in graph[vertex]:
        idx, cost = adj_node
        if visited[idx] is False and dist[idx] > dist[start] + cost:
            dist[idx] = distance + cost
            visited[idx] = True
            heapq.heappush(q, (dist[idx], idx))


for i in range(1, n+1):
    if dist[i] == INF:
        print("INFINITY")
    else:
        print(dist[i])



