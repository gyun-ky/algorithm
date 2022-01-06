import sys
input = sys.stdin.readline
from collections import deque

N = int(input())


data = []
for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(N):
        if data[i][j] == 9:
            data[i][j] = 0
            shark_row = i
            shark_col = j

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs_eating(shark_row, shark_col, cur_size):
    q = deque()
    q.append((shark_row, shark_col, cur_size))
    
    visited = [[-1] * N for r in range(N)]
    visited[shark_row][shark_col] = 0
    eatable = []

    while q:
        y, x, size = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
    
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == -1:
                if data[ny][nx] == size or data[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    
                    q.append((ny, nx, size))

                elif data[ny][nx] < size:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx, size))
                    eatable.append((visited[ny][nx], ny, nx, size))

    if len(eatable) > 0:
        eatable.sort(key = lambda x : (x[0], x[1], x[2]))
        return eatable[0]
    else:
        return (-1, -1, -1, -1)



answer = 0
shark_size = 2
go = True
while go:
    for i in range(shark_size):
        time, s_row, s_col, s_size = bfs_eating(shark_row, shark_col, shark_size)

        if time == -1 and s_col == -1 and s_row == -1 and s_size == -1:
            go = False
            break
        data[s_row][s_col] = 0
        answer += time
        shark_col, shark_row = s_col, s_row
    shark_size += 1


print(answer)

