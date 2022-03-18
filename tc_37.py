# n개의 도시 <= 100
# 한 도시 출발 다른 도시 도착 m개의 버스 <= 100000

# 모든 도시의 쌍 A, B로 가는데에 필요한 비용의 최솟값
import heapq

n = int(input())
m = int(input())

# 결국 버스는 도시간의 단방향 길 ( 도시 사이의 여러개의 )

# city = [[list() for i in range(n+1)] for _ in range(n+1)]

dist = [[int(1e9)] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # heapq.heappush(city[a][b], c)
    dist[a][b] = min(dist[a][b], c)
    

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            dist[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == int(1e9):
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()