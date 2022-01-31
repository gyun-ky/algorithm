
import sys
sys.setrecursionlimit(3000)

N, L, R = map(int, input().split())

A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(row, col, united):
    global pop_sum, visited

    visited[row][col] = True
    united.append((row, col))
    pop_sum += A[row][col]
    for d in range(4):
        ny = row + dy[d]
        nx = col + dx[d]
        if 0<= ny < N and 0<= nx <N:
            if (L <= abs(A[row][col] - A[ny][nx]) <= R) and visited[ny][nx] is False:
                united = dfs(ny, nx, united)
    
    return united


day = 0
while True:
    visited = [[False] * N for _ in range(N)]
    day_continue = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                united = []
                pop_sum = 0
                united = dfs(i, j, united)
                united_len = len(united)
                if united_len != 1:
                    day_continue = True
                    for c in united:
                        A[c[0]][c[1]] = pop_sum // united_len
    
    if day_continue is False:
        break
    else:
        day+=1

print(day)