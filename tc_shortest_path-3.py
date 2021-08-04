import sys
import heapq
input = sys.stdin.readline


INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for i in range(0, N+1)]
distance = [INF] * (N+1)


for _ in range(0, M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, city = heapq.heappop(q)
        if distance[city] > dist:
            continue
        for i in graph[city]:
            cost = dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(C)

cnt = 0
time = 0

for i in range(1, N+1):
    if distance[i] != INF and i!=C:
        cnt +=1
        time = max(time, distance[i])

print(distance)
print(cnt, time)