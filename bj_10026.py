from collections import deque
from re import T

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(str, input().strip())))



answer_a = 0
answer_b = 0
visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for i in range(N):
    for j in range(N):
        if visited1[i][j] is False:
            q = deque()
            visited1[i][j] = True
            q.append((i, j))
            
            while q:
                row, col = q.popleft()

                for d in range(4):
                    ny = row + dy[d]
                    nx = col + dx[d]
                    
                    if 0<= ny < N and 0<= nx < N and visited1[ny][nx] is False and data[row][col] == data[ny][nx]:
                        visited1[ny][nx] = True
                        q.append((ny, nx))
            
            answer_a += 1

        if visited2[i][j] is False:
            q2 = deque()
            visited2[i][j] = True
            q2.append((i, j))

            while q2:
                row, col = q2.popleft()

                for d in range(4):
                    ny = row + dy[d]
                    nx = col + dx[d]

                    if 0<= ny < N and 0<= nx < N and visited2[ny][nx] is False :
                        if (data[row][col] == 'R' and data[ny][nx] == 'G') or (data[row][col] == 'G' and data[ny][nx]=='R') or (data[row][col] == data[ny][nx]):
                            visited2[ny][nx] = True
                            q2.append((ny, nx))


            answer_b += 1

    
print(f'{answer_a} {answer_b}')

