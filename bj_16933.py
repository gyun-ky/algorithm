import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

N, M, K = map(int, input().split())

data = []
for i in range(N):
    data.append(list(map(int, input().strip())))

visited = [[[False for k in range(K+1)] for j in range(M)] for i in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# day가 1이면 낮, 0이면 밤

def bfs():
    q = deque()
    # q = PriorityQueue()
    q.append((1, 0, 0, 0, 1))
    visited[0][0][0] = True

    while q:
        count, col, row, crash_cnt, day = q.popleft()
        
        if col == N-1 and row == M-1:
            return count
        
        for i in range(4):
            ny = col + dy[i]
            nx = row + dx[i]

            if 0<=ny<N and 0<=nx<M:

                # if day == 1:

                #     if data[ny][nx] == 0 and visited[crash_cnt][ny][nx] == False:
                #         q.put((count+1, ny, nx, crash_cnt, 0))
                #         visited[crash_cnt][ny][nx] = True

                #     elif data[ny][nx] == 1 and crash_cnt+1 <= K and visited[crash_cnt+1][ny][nx] == False:
                #         q.put((count+1, ny, nx, crash_cnt+1, 0))
                #         visited[crash_cnt+1][ny][nx] = True
               
                

                # else:
                #     if data[ny][nx] == 0 and visited[crash_cnt][ny][nx] == False:
                #         q.put((count+1, ny, nx, crash_cnt, 1))
                #         visited[crash_cnt][ny][nx] = True
          
                
                #     elif data[ny][nx] == 1 and crash_cnt+1 <= K and visited[crash_cnt+1][ny][nx] == False:
                #         q.put((count+2, ny, nx, crash_cnt+1, 0))
                #         visited[crash_cnt+1][ny][nx] = True

                if data[ny][nx] == 0 and visited[ny][nx][crash_cnt] is False:
                    q.append((count+1, ny, nx, crash_cnt, day*-1))
                    visited[ny][nx][crash_cnt] = True

                elif data[ny][nx] == 1 and crash_cnt+1 <= K and visited[ny][nx][crash_cnt+1] is False:
                    if day == 1:
                        q.append((count+1, ny, nx, crash_cnt+1, day*-1))
                        visited[ny][nx][crash_cnt+1] = True
                    else:
                        q.append((count+1, col, row, crash_cnt, day*-1))
                      
                    

    return -1


print(bfs())
