import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

r1, c1, r2, c2 = map(int, input().split())

visited = [[False]*N for _ in range(N)]

next_r = [-2, -2, 0, 0, 2, 2]
next_c = [-1, 1, -2, 2, -1, 1]
q = deque()

q.append((r1, c1, 0))
visited[r1][c1] = True

while len(q)!=0:
    pos = q.popleft()
    if pos[0] == r2 and pos[1] == c2 :
        print(pos[2])
        exit(0)

    for i in range(6):
        row = pos[0] + next_r[i]
        col = pos[1] + next_c[i]
        if 0<= row <N and 0<= col <N and visited[row][col] == False:
            q.append((row, col, pos[2]+1))
            visited[row][col] = True


print(-1)




    