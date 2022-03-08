# 원숭이는 K번만 말과 같이 움직일 수 있음 -> 나머지는 인접한 칸(상, 하 좌, 우)
# 원숭이는 맨왼쪽 위에서 맨 오른쪽 아래로 이동

# 말의 움직임 (K번만 사용 가능, 장애물 뛰어넘을 수 있음
# 상하좌우로 움직이는 것

# 최소한으로 시작지점에서 도착지점까지 갈 수 있는 방법
from collections import deque

K = int(input())
W, H = map(int, input().split())

grid = []
for _ in range(H):
    grid.append(list(map(int, input().split())))

# 0 평지 / 1은 장애물

# 시간 복잡도
## 200 * 200 = 40000

horse_dx = [2, 1, 2, 1, -1, -2, -1, -2]
horse_dy = [1, 2, -1, -2, 2, 1, -2, -1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



# (row 좌표, col 좌표, 횟수, 말처럼이동가능 남은 횟수)

def bfs():
    visited = [[-1]*W for _ in range(H)]
    q = deque((0, 0, 0, K))
    visited[0][0] = 0

    while q:
        row, col, cnt, horse_move = q.popleft()

        if row == H-1 and col == W-1:
            continue

        # 원숭이 move 일 때,
        for d in range(4):
            nrow = row + dx[d]
            ncol = col + dy[d]

            if nrow<0 or nrow>=H or ncol<0 or ncol>=W or visited[nrow][ncol] != -1 and grid[nrow][ncol] == 1:
                continue

            q.append((nrow, ncol, cnt+1, horse_move))
            visited[nrow][ncol] = cnt+1


        if horse_move > 0:
            for d in range(8):
                nrow = row + dx[d]
                ncol = col + dy[d]

                if nrow<0 or nrow>=H or ncol<0 or ncol>=W :
                    continue

                if visited[nrow][ncol] == -1 or visited[nrow][ncol] > (cnt+1):
                    q.append((nrow, ncol, cnt+1, horse_move-1))
                    visited[nrow][ncol] = cnt+1

    return visited[H-1][W-1]

print(bfs())


    
    