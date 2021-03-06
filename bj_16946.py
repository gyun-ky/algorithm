# bj_16946.py
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

wall = []
for i in range(N):
    wall.append(list(map(int, input().strip())))

answer = [[0 for c in range(M)] for r in range(N)]

# print(wall)
# print(answer)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(col, row):
    global answer
    
    q = deque()
    visited = [[False for c in range(M)] for r in range(N)]

    q.append((col, row))
    visited[col][row] = True

    cnt=1
    
    while q:
        cur = q.popleft()
        for i in range(4):
            ny = cur[0] + dy[i]
            nx = cur[1] + dx[i]

            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx] == True or wall[ny][nx] == 1:
                    continue

                q.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1

    
    
    return cnt


for i in range(N):
    for j in range(M):
        if wall[i][j] != 0:
            answer[i][j] = bfs(i, j) % 10

for i in range(N):
    for j in range(M):
        print(answer[i][j], end="")
    print()

        




