from collections import deque
import sys
inpurt = sys.stdin.readline

INF = int(1e9)

M, N = map(int, input().split()) # M 가로 크기 / N 세로 크기

graph = [list(map(int, input().rstrip()))for _ in range(N)]
dir_col = [1, 0, -1, 0]
dir_row = [0, 1, 0, -1]


queue = deque()
    
def miro(graph):
    
    queue.append([0, 0, 0])
    
    while len(queue) != 0:
        
        pop_room = queue.popleft()
        

        if pop_room[1] == M-1 and pop_room[0] == N-1:
            print(pop_room[2])
            return

        for i in range(0, 4):
            n_row = pop_room[0] + dir_row[i]
            n_col = pop_room[1] + dir_col[i]
            if (0<= n_col <M) and (0<= n_row <N) and graph[n_row][n_col] != -1:
                if graph[n_row][n_col] == 1:
                    graph[n_row][n_col] = -1
                    queue.append([n_row, n_col, pop_room[2]+1]) 
                elif graph[n_row][n_col] == 0:
                    graph[n_row][n_col] = -1
                    queue.appendleft([n_row, n_col, pop_room[2]])


miro(graph)
