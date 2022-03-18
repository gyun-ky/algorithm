# N개의 도시
# 단방향
# C에서 출발 -> 최대한 많은 도시 -> 모두 메시지 받는데에 걸리는 시간 

from dis import dis
import heapq

N, M, C = map(int, input().split())

graph = [list() for _ in range(N+1)]

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dist = [int(1e9)] * (N+1)

def dijkstra(start):
    q = []
    dist[start] = 0
    for v in graph[start]:
        y, z = v
        heapq.heappush(q, (dist[start]+z, y))

    while q:
        cur_cost, vertex = heapq.heappop(q)
        dist[vertex] = cur_cost
        
        for v in graph[vertex]:
            y, z = v
            if dist[y] > cur_cost + z and dist[y] == int(1e9):
                heapq.heappush(q, (cur_cost + z, y))

max_time = 0
cnt = 0

dijkstra(C)

for i in range(N+1):
    if dist[i] != int(1e9):
        cnt+=1
        max_time = max(dist[i], max_time)

print(f'{cnt-1} {max_time}')





        


