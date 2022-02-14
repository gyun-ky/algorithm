
# 낚시왕 오른쪽 1칸 이동
# 낚시왕의 열 중에서 땅과 가장 가까운 상어 잡기 -> 잡으면 상어 사라짐
# 상어 이동 (격자판 넘으면 -> 방향 반대로 바꿔서 속력 유지 이동 / 두마리 이상인 경우 가장 큰 상어가 차지)

# d=1 위 / d=2 아래 / d=3 오른쪽 / d=4 왼쪽

# 낚시왕이 잡고 다음에 상어 이동

from re import S


R, C, M = map(int, input().split())

def check_limit_x(position, d, s):
    # 방향이 4인 경우
    # position-s 가 0보다 큰 경우는 그냥 반환
    if d==4 :
        if position - s > 0 :
            return position - s
        else:
            div = (s - (position-1) ) / (C-1)
            rest = (s - (position-1) ) % (C-1)
            if div % 2 == 1 :
                return C - rest
            else:
                return 1 + rest

    # 아닌 경우
    # 왼쪽으로 갈 때) s에서 (position-1)을 뺀 값에서 (C-1)로 나누었을 떄, 홀수인 경우에는 나머지를 C에서부터 빼주기
    # 짝수인 경우에는 나머지를 1에서부터 더해주기

    # 방향이 3인 경우
    # position+s 가 C 이하인 경우에는 그냥 반환

    if d==3 :
        if position + s <= C :
            return position + s
        else:
            div = (s - (C-position) ) / (C-1)
            rest = (s - (C-position) ) % (C-1)
            if div % 2 == 1 :
                return C - rest
            else:
                return 1 + rest

    # 아닌 경우
    # s에서 (C-position)을 빼주고 그거를 (C-1)로 나누었을 때, 홀수인 경우에는 나머지를 C에서부터 빼주기 
    # 짝수이 경우에는 나머지를 1에서 더해주기


def check_limit_y(position, d, s):
    # 방향이 1인 경우
    # position-s가 0보다 큰 경우는 그냥 반황
    if d==1 :
        if position - s > 0 :
            return position - s
        else:
            div = (s - (position-1) ) / (R-1)
            rest = (s - (position-1) ) % (R-1)
            if div % 2 == 1 :
                return (R - rest)
            else:
                return (1 + rest)
    
    # 아닌 경우
    # s에서 (position-1)을 뺀 값에서 (R-1)로 나누었을 떄, 홀수인 경우 나머지를 R에서부터 빼주기
    # 짝수인 경우에는 나머지를 1에서부터 더해주기

    # 방향이 2인 경우
    # position+s가 R 이하인 경우에는 그냥 반환

    if d==2 :
        if position + s <= R :
            return position + s
        else:
            div = (s - (R-position) ) / (R-1)
            rest = (s - (R-position) ) % (R-1)
            if div % 2 == 1 :
                return (R - rest)
            else:
                return (1 + rest)

    # 아닌 경우
    # s에서 (R-position)을 빼주고 그거를 (R-1)로 나누었을 떄, 홀수인 경우 나머지를 R에서부터 빼주기
    # 짝수인 경우에는 나머지를 1에서부터 더해주기


sharks = []
# r- row, c- col, s - 속력, d - 이동방향, z - 크기

for i in range(M):
    sharks.append(list(map(int, input().split())))

sharks_exist = [True] * M

answer = 0
for p in range(1, C+1):
    
    # p 기준으로 상어 잡기
    for s_idx in range(M):
        if sharks_exist[s_idx] == False:
            continue
        # p와 같은 col에 있는 상어인 경우
        if sharks[s_idx][1] == p:
            answer += sharks[s_idx][4]
            sharks_exist[s_idx] = False


    # 각 water[r][c] = shark의 idx
    water_tmp = [[-1]*(C+1) for _ in range(R+1)]

    # 상어 이동하기
    rmv_shark_idx = []
    for s_idx in range(M):
        if sharks_exist[s_idx] == False:
            continue

        nr, nc = sharks[s_idx][0], sharks[s_idx][1]
        # 위 / 아래 방향인 경우
        if sharks[s_idx][3] == 1 or sharks[s_idx][3] == 2:
            nr = check_limit_y(sharks[s_idx][0], sharks[s_idx][3], sharks[s_idx][2])
        # 오른쪽 / 왼쪽 방향인 경우
        else:
            nc = check_limit_x(sharks[s_idx][1], sharks[s_idx][3], sharks[s_idx][2])

        print(f's_idx : {s_idx} nr, nc = {nr}, {nc}')
        sharks[s_idx][0], sharks[s_idx][1] = nr, nc
        
        if water_tmp[nr][nc] != -1:
            cmp_shark_idx = water_tmp[nr][nc]
            if sharks[cmp_shark_idx][4] > sharks[s_idx][4]:
                rmv_shark_idx.append(s_idx)
            else:
                water_tmp[nr][nc] = s_idx
                rmv_shark_idx.append(cmp_shark_idx)
        else:
            water_tmp[nr][nc] = s_idx

    for rm_idx in rmv_shark_idx:
        sharks_exist[rm_idx] = False
        

print(answer)









