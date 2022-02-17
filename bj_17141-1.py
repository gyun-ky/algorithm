# 연구소의 특정 위치에 바이러스 M개
# N X M  - 0 : 빈칸 / 1 : 벽 / 2 : 바이러스를 놓을 수 있는 칸
# 바이러스는 상하좌우 복제 -> 1초 

# 모든 빈칸에 바이러스를 퍼뜨리는 최소 시간


from itertools import combinations
from collections import deque

# 시간 복잡도
# N = 50 개수 M = 10 2500 * 10 = 25000

N, M = map(int, input().split())

lab_origin = []
virus = []
blank_cnt_static = 0
for i in range(N):
    lab_origin.append(list(map(int, input().split())))
    for j in range(N):
        if lab_origin[i][j] == 2:
            virus.append((i, j))
            blank_cnt_static += 1
        elif lab_origin[i][j] == 0:
            blank_cnt_static += 1


# blank_cnt_static -= M # 빼주지 않는다 추후 큐에서 popleft할 때 빼줄것이다

virus_comb =list(combinations(virus, M))


# 포인트는 바이러스가 여러개라는 것 - 동시에 퍼져나가는 것이기 때문에
# 각 comb마다의 최소 시간을 구하고 
# 각 comb에서 최소시간을 초과시 바로 종료

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


min_time = int(1e9)
for vc in virus_comb:
    visited = [[0]*N for _ in range(N)]
    q = deque()
    for v in vc:
        q.append((v[0], v[1], 0))
        visited[v[0]][v[1]] = -1

    blank_cnt = blank_cnt_static
    
    while q:
        row, col, time = q.popleft()
        blank_cnt-= 1

        if blank_cnt == 0:
            if min_time > time:
                min_time = time
            break
        
        else:
            # if min_time < time:
            #     break

            for d in range(4):
                ny = row + dy[d]
                nx = col + dx[d]

                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
                    if (lab_origin[ny][nx] == 0 or lab_origin[ny][nx] == 2):
                        q.append((ny, nx, time+1))
                        visited[ny][nx] = time+1
                        # blank_cnt -= 1 # 여기서 마지막 빈칸을 없애는 0 처리를 해주게 되면 큐에 들어있는 값이 다음에 걸린다 

    
if min_time == int(1e9):
    print(-1)
else:
    print(min_time)
