
# 낚시왕 오른쪽 1칸 이동
# 낚시왕의 열 중에서 땅과 가장 가까운 상어 잡기 -> 잡으면 상어 사라짐
# 상어 이동 (격자판 넘으면 -> 방향 반대로 바꿔서 속력 유지 이동 / 두마리 이상인 경우 가장 큰 상어가 차지)

# d=1 위 / d=2 아래 / d=3 오른쪽 / d=4 왼쪽

# 낚시왕이 잡고 다음에 상어 이동

R, C, M = map(int, input().split())

def check_limit_x(position, c):
    # - 인 경우
    # 0보다 큰 경우는 그냥 반환

    # 아닌 경우
    # 왼쪽으로 갈 때) 현재 위치에서 (c-1)을 뺀 값에서 (C-1)로 나누었을 떄, 홀수인 경우에는 나머지를 C에서부터 빼주기
    # 짝수인 경우에는 나머지를 1에서부터 더해주기


    # + 인 경우
    # C 이하인 경우에는 그냥 반환

    # 아닌 경우
    # C-c를 빼주고 그거를 (C-1)로 나누었을 때, 홀수인 경우에는 나머지를 C에서부터 빼주기 
    # 짝수이 경우에는 나머지를 1에서부터 더해주기
    

def check_limit_y(position, c)


sharks = []
# r- row, c- col, s - 속력, d - 이동방향, z - 크기

for i in range(M):
    sharks.append(list(map(int, input().split())))

answer = 0
for p in range(1, C+1):
    
    rmv_shark_idx = []
    # p 기준으로 상어 잡기
    for s_idx in range(len(sharks)):
        # p와 같은 col에 있는 상어인 경우
        if sharks[s_idx][1] == p:
            answer += sharks[s_idx][4]
            rmv_shark_idx.append(s_idx)

    # 상어 제거
    for rmv_idx in rmv_shark_idx:
        del sharks[rmv_idx]


    # 각 water[r][c] = shark의 idx
    water_tmp = [[-1]*(C+1) for _ in range(R+1)]

    # 상어 이동하기
    rmv_shark_idx = []
    for s_idx in range(len(sharks)):
        nr, nc = sharks[s_idx][0], sharks[s_idx][1]
        # 위 방향인 경우
        if sharks[s_idx][3] == 1:
            nr = check_limit_y
        # 아래 방향인 경우
        elif sharks[s_idx][3] == 2:
            nr = check_limit_y
        # 오른쪽 방향인 경우
        elif sharks[s_idx][3] == 3:
            nc = check_limit_x
        # 왼쪽 방향인 경우
        elif sharks[s_idx][3] == 4:
            nc = check_limit_x

        if water_tmp[nr][nc] != -1:
            cmp_shark_id = water_tmp[nr][nc]
            if sharks[cmp_shark_id][4] > sharks[s_idx][4]:
                rmv_shark_idx.append(s_idx)
            else:
                water_tmp[nr][nc] = s_idx
                rmv_shark_idx.append(cmp_shark_id)
            


    for rmv_idx in rmv_shark_idx:
        del sharks[rmv_idx]










