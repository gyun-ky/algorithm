from collections import deque

N = None

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = None

def check_boundary(a, b, c, d):
    # 이동한 위치가 지도 안에 있는지 확인
    if 0<=a<N and 0<=b<N and 0<=c<N and 0<=d<N:
        return True
    else:
        return False

def change_rot(shape):
    # 만약 로테이션이면 모양을 바꾸어준다
    if shape == 'v':
        return 'h'
    else:
        return 'v'

def check_visited(a, b, c, d, shape):
    global visited
    
    if shape == 'h':
        s = 0
    else:
        s = 1
        
    if visited[s][a][b] == False and visited[s][c][d] == False:
        # 방문할 것이므로 visited 처리까지 한다
        visited[s][a][b] = True 
        visited[s][c][d] = True
        return True
    else:
        return False
        
        
    

def rotation(rot_num, board, a, b, c, d, shape):
    # 회전 가능 
    # (a,b)(c,d) -> (a+1,b+1)(c,d) 조건 (a+1,b)이 1이 아니어야
    
    ns = change_rot(shape)
    
    if rot_num == 0:
        na, nb = a+1, b+1
        if check_boundary(na, nb, c, d):
            if board[a+1][b] != 1 and check_visited(na, nb, c, d, ns):
                return (True, na, nb, c, d, ns)
            else:
                return (False, a, b, c, d, shape)
    # (a,b)(c,d) -> (a-1,b+1)(c,d) 조건 (a-1,b)가 1이 아니어야
    if rot_num == 1:
        na, nb = a-1, b+1
        if check_boundary(na, nb, c, d) and check_visited(na, nb, c, d, ns):
            if board[a-1][b] != 1:
                return (True, na, nb, c, d, ns)
            else:
                return (False, a, b, c, d, shape)
    # (a,b)(c,d) -> (a,b)(c+1,d-1) 조건 (c+1,d)가 1이 아니어야
    if rot_num == 2:
        nc, nd = c+1, d-1
        if check_boundary(a, b, nc, nd) and check_visited(a, b, nc, nd, ns):
            if board[c+1][d] != 1:
                return (True, a, b, nc, nd, ns)
            else:
                return (False, a, b, c, d, shape)
    # (a,b)(c,d) -> (a,b)(c-1,d-1) 조건 (c-1,d)가 1이 아니어야
    if rot_num == 3:
        nc, nd = c-1, d-1
        if check_boundary(a, b, nc, nd) and check_visited(a, b, nc, nd, ns):
            if board[c-1][d] != 1:
                return (True, a, b, nc, nd, ns)
            else:
                return (False, a, b, c, d, shape)
            
def bfs(board, a, b, c, d, shape):
    
    q = deque()
    q.append([a, b, c, d, 'h', 0])
    visited[0][a][b] = True
    visited[0][c][d] = True
    
    while q:
        ca, cb, cc, cd, s, cnt = q.popleft()
        
        if (ca==N-1 and cb==N-1) or (cc == N-1 and cd == N-1):
            return cnt
        
        for d in range(4):
            na, nb, nc, nd = ca + dx[d], cb + dy[d], cc + dx[d], cd + dy[d]
            
            if check_boundary(na, nb, nc, nd):
                if check_visited(na, nb, nc, nd, s):
                    q.append([na, nb, nc, nd, s, cnt+1])
            
            
            go, na, nb, nc, nd, ns = rotation(d, board, ca, cb, cc, cd, s)
            if go == True:
                q.append([na, nb, nc, nd, ns, cnt+1])
    
    

def solution(board):
    global N, visited
    
    N = len(board[0])
    # visited[0][i][j] - 로봇이 가로로 놓여있을 때 방문 여부 체크
    # visited[1][i][j] - 로봇이 세로로 놓여있을 때 방문 여부 체크
    visited = [[[False]*N for i in range(N)] for k in range(2)]
    
    answer = bfs(board, 0, 0, 0, 1, 'h')
    # N*N 크기 지도 / 1*2 로봇
    # (0,0)(0,1) 부터 시작 -> 0 - 빈칸 / 1 - 벽
    
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
