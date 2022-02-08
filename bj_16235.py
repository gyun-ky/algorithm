
N, M, K = map(int, input().split())

A = []
nut = [[5]*N for _ in range(N)]
for i in range(N):
    A.append(list(map(int, input().split())))

trees = [[] for _ in range(N*N)]

# trees는 1차원 배열이 
for _ in range(M):
    y, x, size = map(int,input().split())
    section_idx = N*(y-1) + (x-1) # 1차원 리스트에 해당하는 idx로 변경
    trees[section_idx].append(size)

# 가을일 때, 움직이는 방향 모음
adj = [
(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) 
]


while K:
    
    for i in range(N):
        for j in range(N):
            section_idx = N*i + j
            trees_len = len(trees[section_idx])
            if  trees_len >= 1:
                trees[section_idx].sort()

                idx = 0
                rm_start_idx = -1
                rm_flag = False
                
                # 봄인 경우
                while idx < trees_len:
                    if rm_flag is False:
                        if nut[i][j] < trees[section_idx][idx]:
                            rm_flag = True
                            rm_start_idx = idx
                        else:
                            nut[i][j] -= trees[section_idx][idx]
                            trees[section_idx][idx] += 1
                    
                    # 여름인 경우 죽은 나무들 처리
                    if rm_flag is True:
                        nut[i][j] += (trees[section_idx][idx] // 2)

                    idx+=1
                
                # 죽은 나무들 제거하고 땅에 나무들 다시 설정
                if rm_flag is True:
                    trees[section_idx] = trees[section_idx][0 : rm_start_idx]
                
              
    for i in range(N):
        for j in range(N):
            section_idx = N*i + j
            # 가을의 경우 5의 배수에 해당하는 나무들 처리
            for age in trees[section_idx]:
                if age % 5 == 0:
                    for dy, dx in adj:
                        ny = i+dy 
                        nx = j+dx
                        if 0<=ny<N and 0<=nx<N:
                            create_trees_idx = N*ny + nx
                            trees[create_trees_idx].append(1)

            # 겨울의 경우 양분 보충
            nut[i][j] += A[i][j]

    K-=1



answer = 0
for section in trees:
    answer += len(section)

print(answer)
            
            
            
            

            