
# 방문 판매원 A는 현재 1번 회사
# X번 회사에 방문해 물건 판매

# 2개의 회사는 양방향 이동 가능
# 1만큼의 cost

# 소개팅 상대 K번 회사 에 존재
# 1번 -> K번 -> X번 회사

# 플로이드 워셜을 이용해야!!!!

N, M = map(int, input().split())

dist = [[int(1e9)]* (N+1) for _ in range(N+1)] # dist - i, j 와의 최소 거리 

for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            dist[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

X, K = map(int, input().split())

# dist[i][j] = min(dist[i][k] + dist[k][j]) k = i ~ j

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            


if dist[1][K] + dist[K][X] >= int(1e9):
    print(-1)
else:
    print(dist[1][K] + dist[K][X])









