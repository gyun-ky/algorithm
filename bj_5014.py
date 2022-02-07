from collections import deque

F, S, G, U, D = map(int, input().split())

q = deque()
visited = set()
visited.add(S)
q.append((S, 0))

while q:
    cur, cnt = q.popleft()
    if cur == G:
        print(cnt)
        exit(0)
    
    if (1<= cur + U <= F) and (cur+U not in visited):
        visited.add(cur+U)
        q.append((cur+U, cnt+1))

    if (1<= cur - D <= F) and (cur-D not in visited):
        visited.add(cur-D)
        q.append((cur-D, cnt+1))

print('use the stairs')