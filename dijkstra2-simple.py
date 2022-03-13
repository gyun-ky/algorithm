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


for g in graph:
    g.sort(key= lambda x:(x[1], x[0]))


visited = [False] * (n+1)
visited[0] = True

dist = [int(1e9)] * (n+1)
dist[start] = 0

while (False in visited):

    visited[start] = True

    for adj_node in graph[start]:
        idx, cost = adj_node
        if visited[idx] is False and dist[idx] > dist[start] + cost:
            dist[idx] = dist[start] + cost
    
    # 현재 방문하지 않은 vertex 중에서 가장 최단 거리인 vertex를 찾아주는 것 -> 이 부분에서 시간이 선형적으로 찾으면서 오래걸린다
    min = int(1e9)
    for i in range(1, n+1):
        if visited[i] is False and min > dist[i]:
            min = dist[i]
            start = i


    # 이부분만 개선 시킨다면? 


for i in range(1, n+1):
    if dist[i] == INF:
        print("INFINITY")
    else:
        print(dist[i])
#gi


