import itertools
import copy
from collections import deque
# import sys
# input = sys.stdin.readline

group = list(map(int, input().split()))

s = sum(group)

visited = [[False]*(1501) for _ in range(1501)]

# dfs로 진행하면 안될 놈에게 계속 하게되는 함정이 있다

# 크기가 다른 두개를 선택하는 것이기 떄문에 combination을 사용한다


# 돌 그룹 개수가 같아지지 않다는 것을 알려면 어케?
    # --> 다시 원래 group으로 돌아온다? 아님 큐가 0가 된다?


q = deque()
q.append(group)
visited[group[0]][group[1]] = True

if group[0] == group[1] == group[2] :
    print(1)
    exit(0)


while q:
    cur_group = q.popleft()
    group_idx_comb = [(0,1), (0,2), (1,2)]

    
    for g in group_idx_comb:

        # 두 조합이 같다면 패스
        if cur_group[g[0]] == cur_group[g[1]]:
            continue

        new_group = copy.deepcopy(cur_group)

        # 큰쪽 작은쪽 비교
        if cur_group[g[0]] < cur_group[g[1]]:
            # if cur_group[g[0]] * 2 == cur_group[g[1]] :
            #     continue
            new_group[g[1]] = new_group[g[1]] - new_group[g[0]]
            new_group[g[0]] = new_group[g[0]]*2
        else:
            # if cur_group[g[1]] * 2 == cur_group[g[0]] :
            #     continue
            new_group[g[0]] = new_group[g[0]] - new_group[g[1]]
            new_group[g[1]] = new_group[g[1]]*2
        
        if visited[new_group[0]][new_group[1]] == True:
            continue
        
    
        # 세그룹이 모두 같다면
        if new_group[0] == new_group[1] == new_group[2]:
            print(1)
            exit(0)

        q.append(new_group)
        visited[new_group[0]][new_group[1]] = True

print(0)