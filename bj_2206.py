from collections import deque
import sys
input = sys.stdin.readline
max_num = int(1e9)

N, M = map(int, input().split())

visited = [[[max_num for col in range(M)] for row in range(N)] for depth in range(2)]
# visited[row][col][0] : 벽 1회 깨기 전의 방문 최소 cnt 횟수
# visited[row][col][1] : 벽 1회 꺠기 후의 방문 최소 cnt 횟수


data = []

for _ in range(N):
    data.append(list(map(int, input().strip())))




dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


# (0, 0)부터 시작해서 (N-1, M-1) 까지 가는 것으로
q = deque()


def bfs(col, row, cnt):

    q.append((col, row, cnt, False))
    visited[0][col][row] = cnt

    while q:

        cur = q.popleft()
        
        for d in range(4):
            ny = cur[0] + dy[d]
            nx = cur[1] + dx[d]

            if ny<0 or ny>=N or nx<0 or nx>=M:
                continue

            if ny == N-1 and nx == M-1:
                if cur[3] == False:
                    visited[0][ny][nx] = min(visited[0][ny][nx], cur[2]+1)
                else:
                    visited[1][ny][nx]= min(visited[1][ny][nx], cur[2]+1)

                continue

            
            # 1번 벽 깨기를 하지 않은 경우
            if cur[3] == False:
                # 1번도 벽깨기 안한 경우, 벽을 만나면 방문하지 않은 벽일 경우 깨기
                if data[ny][nx] == 1 and visited[1][ny][nx] == int(1e9):
                    visited[1][ny][nx] = cur[2]+1
                    q.append((ny, nx, cur[2]+1, True))
                
                # 1번도 벽깨기 안한 경우, 빈칸을 만나면 방문하지 않은 경우 진입
                if data[ny][nx] == 0 and visited[0][ny][nx] == int(1e9):
                    visited[0][ny][nx] = cur[2]+1
                    q.append((ny, nx, cur[2]+1, False))

            # 1번 이상 벽깨기를 한 후인 경우
            else:
                # 1번 이상 벽꺠기를 한 경우, 빈칸을 만나면 진행
                if data[ny][nx] == 0 and visited[1][ny][nx] == int(1e9):
                    visited[1][ny][nx] = cur[2]+1
                    q.append((ny, nx, cur[2]+1, True))

                # 1번이상 벽깨기 한 경우, 빈칸 아닌거 만나면 진행 X


    return min(visited[0][N-1][M-1], visited[1][N-1][M-1])

result = bfs(0, 0, 1)
if result == int(1e9):
    print(-1)
else:
    print(result)
