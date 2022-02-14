
# 낚시왕 오른쪽 1칸 이동
# 낚시왕의 열 중에서 땅과 가장 가까운 상어 잡기 -> 잡으면 상어 사라짐
# 상어 이동 (격자판 넘으면 -> 방향 반대로 바꿔서 속력 유지 이동 / 두마리 이상인 경우 가장 큰 상어가 차지)

# d=1 위 / d=2 아래 / d=3 오른쪽 / d=4 왼쪽

# 낚시왕이 잡고 다음에 상어 이동


R, C, M = map(int, input().split())

class Shark:
    def __init__(self, row, col, size=0, speed=0, direction=0):
        self.row = row
        self.col = col
        self.size = size
        self.speed = speed
        self.direction = direction
    

def check_limit_x(position, d, s):
    # 좌우 (행) 으로 움직일 때, 다음 위치 추정 메소드
    while s:
        if d == 4:
            position -=1
            if position == 0:
                position += 2
                d = 3

        else:
            position += 1
            if position == C+1:
                position -= 2
                d = 4

        s-=1

    return (position, d)



def check_limit_y(position, d, s):
    # 위아래 (열)로 움직였을 때, 다음 위치 추정 메소드
    while s:
        if d == 1:
            position -=1
            if position == 0:
                position += 2
                d = 2
        else:
            position += 1
            if position == R+1:
                position -= 2
                d= 1
        
        s-=1

    return (position, d)

   



sharks = []

for i in range(M):
    # r- row, c- col, s - 속력, d - 이동방향, z - 크기
    r, c, s, d, z = map(int, input().split())
    sharks.append(Shark(r, c, z, s, d))

sharks_exist = [True] * M

answer = 0
for p in range(1, C+1):
    
    # p 기준으로 상어 잡기 / 행이 가장 작은 값을 가지는 아이로
    min_row = int(1e9)
    catch_idx = -1
    for s_idx in range(M):
        if sharks_exist[s_idx] == False:
            continue
        
        # p와 같은 col에 있는 상어인 경우
        if sharks[s_idx].col == p and min_row > sharks[s_idx].row:
            min_row = sharks[s_idx].row
            catch_idx = s_idx
            
    if catch_idx != -1:
        answer += sharks[catch_idx].size
        sharks_exist[catch_idx] = False


    # 각 water[r][c] = shark의 idx
    water_tmp = [[-1]*(C+1) for _ in range(R+1)]

    # 상어 이동하기
    rmv_shark_idx = []
    for s_idx in range(M):
        if sharks_exist[s_idx] == False:
            continue

        nr, nc = sharks[s_idx].row, sharks[s_idx].col
        # 위 / 아래 방향인 경우
        if sharks[s_idx].direction == 1 or sharks[s_idx].direction == 2:
            nr, nd = check_limit_y(sharks[s_idx].row, sharks[s_idx].direction, sharks[s_idx].speed)
        # 오른쪽 / 왼쪽 방향인 경우
        else:
            nc, nd = check_limit_x(sharks[s_idx].col, sharks[s_idx].direction, sharks[s_idx].speed)

        sharks[s_idx].row, sharks[s_idx].col, sharks[s_idx].direction = nr, nc, nd

        if water_tmp[nr][nc] != -1:
            cmp_shark_idx = water_tmp[nr][nc]
            if sharks[cmp_shark_idx].size > sharks[s_idx].size:
                rmv_shark_idx.append(s_idx)
            else:
                water_tmp[nr][nc] = s_idx
                rmv_shark_idx.append(cmp_shark_idx)
        else:
            water_tmp[nr][nc] = s_idx

    for rm_idx in rmv_shark_idx:
        sharks_exist[rm_idx] = False
        

print(answer)









