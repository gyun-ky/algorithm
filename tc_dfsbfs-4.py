from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# Visited는 따로 생성하지 않고 방문시, 1->0으로 변경

direct_row = [0, 1, 0, -1]
direct_col = [1, 0, -1, 0]

def bfs(row, col):
    q = deque()
    cnt = 1
    q.append([row, col, cnt])
    while len(q) != 0 :
        nxt = q.popleft()
        for d in range(4):
            new_node = [nxt[0] + direct_row[d], nxt[1] + direct_col[d], nxt[2] + 1]
            if new_node[0]<0 or new_node[0]>=N or new_node[1]<0 or new_node[1]>=M:
                continue
            if graph[new_node[0]][new_node[1]] == 1:
                if new_node[0] == N-1 and new_node[1] == M-1:
                    return new_node[2]
                else:
                    graph[new_node[0]][new_node[1]] = 0
                    q.append(new_node)


print(bfs(0,0))




 

        



