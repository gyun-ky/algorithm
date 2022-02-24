from collections import deque

N, M = map(int, input().split())
wall = []
for _ in range(M):
    wall.append(list(map(int, input().split())))

visited = [[0]*N for _ in range(M)]
room_size = [0]# room 은 idx 1부터 들어감

# 서쪽 1, 북쪽 2, 동쪽 4, 남쪽 8
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(i, j, room_idx):
    q = deque()
    q.append((i, j))
    size = 0
    visited[i][j] = room_idx
#
    while q:
        row, col = q.popleft()
        size += 1

        for d in range(4):
            nrow = row + dx[d]
            ncol = col + dy[d]

            if nrow < 0 or nrow >=M or ncol < 0 or ncol >= N :
                continue
            
            if (wall[row][col] & (1<<d)) > 0: 
                # 해당 방향에 벽이 존재한다는 뜻
                continue

            if visited[nrow][ncol] == 0:
                q.append((nrow, ncol))
                visited[nrow][ncol] = room_idx

    return size


max_room_size = 0
room_idx = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            room_idx += 1
            size = bfs(i, j, room_idx)
            max_room_size = max(size, max_room_size)
            room_size.append(size)

max_integrated_room = 0
for i in range(M):
    for j in range(N):
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if nx < 0 or nx >=M or ny < 0 or ny >= N :
                continue


            if visited[i][j] != visited[nx][ny]:
                max_integrated_room = max(max_integrated_room, room_size[visited[nx][ny]] + room_size[visited[i][j]])


print(room_idx)
print(max_room_size)
print(max_integrated_room)



