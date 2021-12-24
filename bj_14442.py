import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

visited = [[[0 for col in range(M)] for row in range(N)]for depth in range(K+1)]

data = []
for col in range(N):
    data.append(list(map(int, input().strip())))



dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(col, row):
    q = deque()
    visited[0][col][row]= 1
    q.append((col, row, 0))

    while q:
        c, r, crash_cnt = q.popleft()

        if c == N-1 and r == M-1:
            return visited[crash_cnt][c][r]

        for i in range(4):
            nc = c + dy[i]
            nr = r + dx[i]

            if nc < 0 or nc >= N or nr < 0 or nr >= M:
                continue
 
            if data[nc][nr] == 0 and visited[crash_cnt][nc][nr]==0: # 벽이 아닌 경우
                q.append((nc, nr, crash_cnt))
                visited[crash_cnt][nc][nr] = visited[crash_cnt][c][r]+1

            if data[nc][nr] == 1 and crash_cnt+1 <= K and visited[crash_cnt+1][nc][nr] == 0: # 벽인 경우
                q.append((nc, nr, crash_cnt+1))
                visited[crash_cnt+1][nc][nr] = visited[crash_cnt][c][r]+1
                
    return -1


print(bfs(0, 0))



