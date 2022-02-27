# 칸은 꺠긋한 칸 / 더러운 칸
# 청소기 더러운칸 -> 깨끗한 칸

# 가구가 놓여진 칸으로 이동 불가

# 인접한 칸 이동, 같은 칸 여러번 방문 가능

# 더러운 칸을 모두 깨끗한 칸으로 만드는 데에 필요한 이동 횟수의 최소값

# q (i, j, 이동 횟수, 치운 더러운 방 횟수)

from collections import deque
from itertools import permutations


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(start_x, start_y, w, h):
    

    q = deque()
    q.append((start_x, start_y, 0))

    dist = [[int(1e9)] * w for _ in range(h)]
    dist[start_x][start_y] = 0
        
    while q:
        row, col, cnt = q.popleft()


        for d in range(4):
            nrow = row + dx[d]
            ncol = col + dy[d]
            
            # 범위를 벗어난다면
            if 0 > nrow or nrow >= h or 0 > ncol or ncol >= w or room_map[nrow][ncol] == 'x' or dist[nrow][ncol] < (cnt+1):
                continue
                
            # 가구가 있는 칸이라면 
            if room_map[nrow][ncol] == 'x':
                dist[nrow][ncol] = -1

            # 이미 방문하였는데 더 낮은 이동 횟수가 있다면
            if dist[nrow][ncol] <= (cnt+1):
                continue
            # 이동해온 것이 더 낮다면
            else:
                q.append((nrow, ncol, cnt+1))
                dist[nrow][ncol] = cnt+1
                

    return dist


        

while True:
    w, h = map(int, input().split())
    dirty = []
    
    if w == 0 and h == 0:
        break

    room_map = []
    for i in range(h):
        room_map.append(list(map(str, input().strip())))
        for j in range(w):
            if room_map[i][j] == '*':
                dirty.append((i, j))
            if room_map[i][j] == 'o':
                start_x, start_y = i, j

    start_dist = bfs(start_x, start_y, w, h)

    # dirty의 0 idx 부터 마지막 idx까지의 시작점 기준 해당 idx 부터 bfs 한 배열
    each_node_dist_list = []
    for i in range(len(dirty)):
        each_node_dist_list.append(bfs(dirty[i][0], dirty[i][1], w, h))

    dirty_idx = [i for i ]
    permutation_dirty_list = list(permutations(dirty, len(dirty)))

    ans = int(1e9)

    for p in permutation_dirty_list:
        


    if ans == int(1e9):
        print(-1)
    else:
        print(ans)




