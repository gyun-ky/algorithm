
# 가을일 때, 움직이는 방향 모음
adj = [
(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) 
]

N, M, K = map(int, input().split())

A = []
nut = [[5]*N for _ in range(N)]
for i in range(N):
    A.append(list(map(int, input().split())))

trees = [[[] for j in range(N)]for i in range(N)]

for _ in range(M):
    y, x, size = map(int,input().split())
    trees[y-1][x-1].append(size)

while K:
    p = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 나무들의 크기 조정이 다 끝난 후 대체할 임시 리스트
            tmp = []
            
            trees[i][j].sort()
            for t in trees[i][j]:
                if t <= nut[i][j]:
                    nut[i][j] -= t 
                    tmp.append(t+1)
                        
                    # 가을 처리까지 한꺼번에
                    if (t+1) % 5 == 0:
                        for dy, dx in adj:
                            ny = i+dy 
                            nx = j+dx
                            if 0<=ny<N and 0<=nx<N:
                                p[nx][ny] += 1 # 인접한 8개의 칸에 나이가 1인 나무가 생길것을 p에 모두 저장 
                                # 미래의 일이 현재에 영향을 미치지 않기 위해 p에 저장해두었다과 일괄 처리
                else:
                    nut[i][j] += t//2
                
            # 사이즈가 변경된 나무들로 대체
            trees[i][j] = tmp
            nut[i][j] += A[i][j]

    for i in range(N):
        for j in range(N):
            for _ in range(p[i][j]):
                trees[i][j].append(1)

    K-=1

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])


print(answer)

