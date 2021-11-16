import sys
from collections import deque
import copy
import itertools as it

max_safe = 0

input = sys.stdin.readline

N, M = map(int, input().split())

data = []

blank = []

virus = []

wall_cnt = 0
init_virus_cnt = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(M):
        if data[i][j] == 0:
            blank.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))
            init_virus_cnt += 1
        else:
            wall_cnt += 1

comb_wall = list(it.combinations(blank, 3))
# 시간복잡도 : 64 * 63 * 62 *64 = 15,998,976

# print(f'wall_cnt = {wall_cnt}')
# print(f'init_virus_cnt = {init_virus_cnt}')

for comb in comb_wall:
    data_cpy = copy.deepcopy(data)
    for i in range(3):
        data_cpy[comb[i][0]][comb[i][1]] = 1

    virus_cnt = init_virus_cnt

    for v in virus:
        q = deque()
        q.append((v[0], v[1], virus_cnt))
        while len(q) != 0:
            loc = q.popleft()
            for d in range(4):
                ny = loc[0]+dy[d]
                nx = loc[1]+dx[d]
                if 0<=ny<N and 0<=nx<M:
                    if data_cpy[ny][nx]==0:
                        data_cpy[ny][nx] = 2
                        virus_cnt += 1
                        q.append((ny, nx, loc[2]+1))

    max_safe = max(max_safe, N*M-virus_cnt-3-wall_cnt)

print(max_safe)

 


