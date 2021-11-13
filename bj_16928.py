import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

box = [0] * 101

for _ in range(N+M):
    start, dest = map(int, input().split())
    box[start] = dest

q = deque()

visited = [False]*101

# 큐에 들어갈 튜플 (위치, 횟수)

q.append((1,0))
visited[1] = True

while len(q) != 0:
    
    cur_pos_cnt = q.popleft()
    if cur_pos_cnt[0] == 100:
        print(cur_pos_cnt[1])
        break


    for dice in range(1, 7):
        moved_pos = cur_pos_cnt[0] + dice

        if moved_pos > 100:
            continue
        else:
            if visited[moved_pos] == True:
                continue
            else :
                visited[moved_pos] = True
                if box[moved_pos] != 0:
                    q.append((box[moved_pos], cur_pos_cnt[1]+1))
                else:        
                    q.append((moved_pos, cur_pos_cnt[1]+1))





