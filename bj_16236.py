import sys
from collections import deque
input = sys.stdin.readline

# 아기상어 처음 크기 2 
# 1초에 상하좌우 한칸씩 이동
# 자신의 크기보다 큰 물고기 칸 못지나감
# 자신의 크기보다 작은 물고기 먹을 수 있음
    # 물고기 먹을 때 마다 크기 1 증가
# 자신의 크기와 같은 물고기 칸은 먹을수는 없지만 지나갈 수 있음

#먹을수있는 물고기가 없는 경우 -> 엄마상어에게 도움 요청
#먹을 수 있는 물고기 1 -> 물고기 먹으러 감
#먹을 수 있는 물고기 1 초과 -> 거리가 가까운 물고기 먹으러감 - bfs
    # 거리 = 이동 최소 칸의 수
    # 거리 같은 물고기 많다면 - 가장 위 물고기 > 가장 왼쪽 물고기


# 몇초동안 물고기를 다 먹을 수 있는지

N = int(input())

space = []
fish_cnt = 0
for i in range(N):
    space.append(list(map(int, input().split())))
    for j in range(N):
        if space[i][j] == 9:
            space[i][j] = 0
            row, col = i, j
        if space[i][j] != 9 and space[i][j] != 0:
            fish_cnt+=1

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
# visited = [[[False for t in range(N*N*N)]for c in range(N)]for r in range(N)]
print(fish_cnt)
print(space)

def bfs(i, j):
    global fish_cnt
    q = deque()
    q_hit = []
    q.append((i, j, 2, 0))
    visited = [[False for c in range(N)]for r in range(N)]
    visited[i][j] = 0
    min_time = int(1e9)

    while q:
        row, col, size, time = q.popleft()

        if fish_cnt == 0:
            return time

        
        for i in range(4):
            ny = row + dy[i]
            nx = col + dx[i]

            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == False:
                 
                # 아무것도 없는 경우
                if space[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx, size, time+1))
                    continue

                # 큰 물고기 만났을 때,
                if space[ny][nx] > size:
                    continue

                # 작은 물고기 만났을 때, 
                if space[ny][nx] < size and space[ny][nx] != 0:
                    fish_cnt -= 1
                    space[ny][nx] = 0
                    visited = [[False for c in range(N)]for r in range(N)]
                    q.clear()
                    q.append((ny, nx, size+1, time+1))
                    break
                
                # 같은 물고기 만났을 때,
                if space[ny][nx] == size:
                    visited[ny][nx] = True
                    q.append((ny, nx, size, time+1))

    return 0






print(bfs(row, col))
print(space)