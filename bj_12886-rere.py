from collections import deque

group = list(map(int, input().split()))

s = sum(group)

visited = [[False]*(1501) for _ in range(1501)]

group_idx_comb = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]

def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))
    visited[a][b] = True
    
    while q:
        cur = q.popleft()

        if cur[0] == cur[1] == cur[2]:
            print(1)
            return

        for g in group_idx_comb:
            new_group = [0]*3
            if cur[g[0]] == cur[g[1]]:
                continue
            elif cur[g[0]] < cur[g[1]]:
                new_group[g[1]] = cur[g[1]] - cur[g[0]]
                new_group[g[0]] = cur[g[0]]*2
                new_group[g[2]] = cur[g[2]]
            else:
                new_group[g[0]] = cur[g[0]] - cur[g[1]]
                new_group[g[1]] = cur[g[1]]*2
                new_group[g[2]] = cur[g[2]]

            if visited[new_group[0]][new_group[1]] == True:
                continue

            q.append(new_group)
            visited[new_group[0]][new_group[1]] = True

    print(0)




if s%3 != 0: print(0)
else:
    bfs(group[0], group[1], group[2])


        
        
        

