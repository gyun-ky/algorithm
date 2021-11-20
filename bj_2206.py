from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

crash_visited = [[False]*M]*N
not_crash_visited = [[False]*M]*N

data = []

for _ in range(N):
    data.append(list(map(int, input().strip())))

print(data)
print(crash_visited)
print(not_crash_visited)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


# (0, 0)부터 시작해서 (N-1, M-1) 까지 가는 것으로
q = deque()

min_cnt = int(1e9)

def bfs(col, row, cnt):
    global min_cnt

    q.append((col, row, cnt, False))
    not_crash_visited[col][row] = True
    crash_visited[col][row] = True

    while q:

        cur = q.popleft()
        
        for d in range(4):
            ny = cur[0] + dy[d]
            nx = cur[1] + dx[d]

            if ny<0 or ny>=N or nx<0 or nx>=M:
                continue

            if ny == N-1 and nx == M-1:
                print("여기 왔다")
                min_cnt = min(min_cnt, cur[2])
                continue

            if data[ny][nx] == 0:
                
                if cur[3] == False and not_crash_visited[ny][nx] == False:
                    q.append((ny, nx, cur[2]+1, False))
                    not_crash_visited[ny][nx] = True

                elif cur[3] == True and crash_visited[ny][nx] == False:
                    q.append((ny, nx, cur[2]+1, True))
                    crash_visited[ny][nx] = True

            if data[ny][nx] == 1 and cur[3] == False:
                q.append((ny, nx, cur[2]+1, True))
            

bfs(0, 0, 1)

if min_cnt == int(1e9):
    print(-1)
