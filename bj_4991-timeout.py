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

# 가로 크기 w / 세로 크기 h
def bfs(start_x, start_y, w, h, permutation):
    
    move_total = 0
    for p_idx in range(len(permutation)):
        if (p_idx -1) == -1:
            sr,sc = start_x, start_y
        else:
            sr, sc = permutation[p_idx-1]
        dr, dc = permutation[p_idx]

        q = deque()
        q.append((sr, sc, 0))
        visited = [[False] * w for _ in range(h)]
        
        flag = False
        while q:
            row, col, cnt = q.popleft()

            if row == dr and col == dc:
                flag = True
                move_total += cnt
                break

            for d in range(4):
                nrow = row + dx[d]
                ncol = col + dy[d]

                if 0 > nrow or nrow >= h or 0 > ncol or ncol >= w or room_map[nrow][ncol] == 'x' or visited[nrow][ncol] is True:
                    continue
                
                # 도착지가 아닌데 더러운 방이라면 
                if room_map[nrow][ncol] == '*' and  (nrow != dr and ncol != dc):
                    continue
                
                # 그 외의 경우
                else:
                    q.append((nrow, ncol, cnt+1))
                    visited[nrow][ncol] = True

            # 도착지까지 갈 수 없다면 (경로가 끊긴 것임)
        if flag is False:
            return -1

    return move_total


        

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

    permutation_dirty_list = list(permutations(dirty, len(dirty)))

    ans = int(1e9)

    for p in permutation_dirty_list:
        tmp_ans = bfs(start_x, start_y, w, h, p)
        if tmp_ans == -1:
            continue
        else:
            ans = min(ans, tmp_ans)


    if ans == int(1e9):
        print(-1)
    else:
        print(ans)




