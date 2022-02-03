import sys
# input = sys.stdin.readline()

N, M, K = map(int, input().split())

A = []
nut = []
for i in range(N):
    A.append(list(map(int, input().split())))
    nut.append(A[i])


trees = [[] for _ in range(N*N)]

for _ in range(M):
    y, x, size = map(int,input().split())
    section_idx = N*(y-1) + (x-1)
    trees[section_idx].append(size)

adj = [
(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) 
]

while K:
    
    for i in range(N):
        for j in range(N):
            section_idx = N*i + j
            trees_len = len(trees[section_idx])
            if  trees_len > 1:
                trees[section_idx].sort()
            
            rm_start_idx = trees_len-1
            for t_idx in range(trees_len):
                if nut[i][j] < trees[section_idx][t_idx]:
                    rm_start_idx = t_idx
                    break
                nut[i][j] -= trees[section_idx][t_idx]
                trees[section_idx][t_idx] += 1

            for _ in range(rm_start_idx, trees_len):
                nut[i][j] += (trees[section_idx][rm_start_idx] // 2)
                del trees[section_idx][rm_start_idx]

    for i in range(N):
        for j in range(N):
            section_idx = N*i + j

            for age in trees[section_idx]:
                if age % 5 == 0:
                    for dy, dx in adj:
                        ny = i+dy 
                        nx = j+dx
                        if 0<=ny<N and 0<=nx<N:
                            create_trees_idx = N*ny + nx
                            trees[create_trees_idx].append(1)

            nut[i][j] += A[i][j]

    K-=1

answer = 0
for section in trees:
    answer += len(section)

print(answer)
            
            
            
            

            