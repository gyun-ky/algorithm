import sys
from collections import deque
input = sys.stdin.readline

chess = []
for i in range(8):
    chess.append(list(map(str, input().strip())))



#오위 오 오아 아 아왼 왼 왼위 위 
dy = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
dx = [1, 1, 1, 0, -1, -1, -1, 0, 0]

visited = [[False]* 8 for r in range(8)]

def bfs():
    q = deque()
    q.append((7, 0, 0))
    time_save = 0
    visited[7][0] = True

    while q:
        y, x, time = q.popleft()

        if time > time_save:
            chess.pop()
            chess.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])
            time_save = time
        
        if y==0:
            return 1
        
        for i in range(9):
            ny = y + dy[i]
            nx = x + dx[i]


            if 0<=ny<8 and 0<=nx<8 and chess[ny][nx] == '.':
                if i == 8:
                    q.append((ny, nx, time+1))
                elif chess[y][x] == '.':
                    visited[ny][nx] == True
                    q.append((ny, nx, time+1))
        
    return 0


print(bfs())