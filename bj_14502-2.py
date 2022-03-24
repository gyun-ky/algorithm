# 0- 빈칸 / 1- 벽 / 2- 바이러스
from itertools import combinations
from copy import deepcopy
from collections import deque

N, M = map(int, input().split())

# 세로 - N, 가로 - M

lab = []
blank = []
virus = []

for i in range(N):
    lab.append(list(map(int, input().split())))
    for j in range(M):
        if lab[i][j] == 0:
            blank.append((i, j))
        if lab[i][j] == 2:
            virus.append((i, j))

blank_cnt = len(blank)

perm = list(combinations(blank, 3))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
for p in perm:
    visited = [[False]*M for _ in range(N)]
    n_lab = deepcopy(lab)
    for i, j in p:
        n_lab[i][j] = 1
    
    size = blank_cnt - 3

    
    for v in virus:
        q = deque()
        visited[v[0]][v[1]] = True
        q.append(v)

        while q:
            row, col = q.popleft()

            for d in range(4):
                nrow = row + dy[d]
                ncol = col + dx[d]

                if nrow >=N or ncol >= M or nrow < 0 or ncol < 0:
                    continue
                
                if visited[nrow][ncol] is False and n_lab[nrow][ncol] == 0:
                    visited[nrow][ncol] = True
                    size -= 1
                    q.append((nrow, ncol))
#
    answer = max(answer, size)

print(answer)

