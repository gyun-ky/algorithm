import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

visited = [[False for c in range(M)]for r in range(N)]

data = []
q = deque()
not_well_tomato = 0
blank = 0
for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(M):
        if data[i][j] == 1:
            visited[i][j] = True
            q.append((i, j, 0))
        elif data[i][j] == 0:
            not_well_tomato += 1
        

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs():
    global q, not_well_tomato
    
    while q:
        row, col, time = q.popleft()
        
        for i in range(4):
            ny = row + dy[i]
            nx = col + dx[i]

            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == False:
                if data[ny][nx] == -1 or data[ny][nx] == 1:
                    visited[ny][nx] = True
                    continue

                if data[ny][nx] == 0:
                    data[ny][nx] = 1
                    visited[ny][nx] = True
                    not_well_tomato -= 1
                    if not_well_tomato == 0 :
                        return time+1
                    q.append((ny, nx, time+1))
    
    return -1

if not_well_tomato == 0:
    print(0)
else:
    print(bfs())