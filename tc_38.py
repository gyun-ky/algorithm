# 성적을 비교한 일부만 가짐
# 학생 N명
# A 번 학생이 B번 학생보다 낮을 시 A->B

# 성적 순위를 정확히 알 수 있는 학생은?
# 결국 해당 start node에서 다른 node까지 갈 수 있는가?
# 양방향 그래프로 표현

import heapq

INF = int(1e9)

N, M = map(int, input().split())

dist = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, = map(int, input().split())
    dist[a][b] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        dist[a][b] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


answer = 0
for i in range(1, N+1):
    connected = [False] * (N+1)
    connected[0] = True
    connected[i] = True
    for j in range(1, N+1):
        if dist[i][j] != INF:
            connected[j] = True
        elif dist[j][i] != INF:
            connected[j] = True
        
    if False not in connected:
        answer += 1

print(answer)

