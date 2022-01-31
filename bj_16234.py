from collections import deque

N, L, R = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

day = 0
while True:

    move = False
    visited = [[False]*N for _ in range(N)]
    total_visit = N*N

    for r in range(N):
        for c in range(N):
            if visited[r][c] == True:
                continue
            q = deque()
            q.append((r,c))
            united = [(r, c)]
            people_sum = A[r][c]
            visited[r][c] = True

            while q:
                y, x = q.popleft()

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0<= ny < N and 0 <= nx < N and visited[ny][nx] == False:
                        if L<= abs(A[ny][nx] - A[y][x]) <= R:
                            q.append((ny, nx))
                            united.append((ny, nx))
                            people_sum += A[ny][nx]
                            visited[ny][nx] = True


            if len(united) == 1:
                continue
            else:
                move = True
                after_cnt = people_sum//len(united)
                for n in united:
                    A[n[0]][n[1]] = after_cnt
            
    if move is True:
        day+=1
    else:
        break

print(day)