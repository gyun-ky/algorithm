
# 낚시왕 오른쪽 1칸 이동
# 낚시왕의 열 중에서 땅과 가장 가까운 상어 잡기 -> 잡으면 상어 사라짐
# 상어 이동 (격자판 넘으면 -> 방향 반대로 바꿔서 속력 유지 이동 / 두마리 이상인 경우 가장 큰 상어가 차지)

# d=1 위 / d=2 아래 / d=3 오른쪽 / d=4 왼쪽

# 낚시왕이 잡고 다음에 상어 이동


from operator import ne


R, C, M = map(int, input().split())

class Shark:
    def __init__(self, size=0, speed=0, direction=0):
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

   

cur_sharks = [[Shark() for j in range(C+1)] for i in range(R+1)]



for i in range(M):
    # r- row, c- col, s - 속력, d - 이동방향, z - 크기
    r, c, s, d, z = map(int, input().split())
    cur_sharks[r][c] = Shark(z, s, d)


answer = 0
for p in range(1, C+1):
    
    # p 기준으로 상어 잡기 / 행이 가장 작은 값을 가지는 아이로
    for i in range(1, R+1):
        if cur_sharks[i][p].size != 0:
            answer += cur_sharks[i][p].size
            cur_sharks[i][p] = Shark()
            break


    # 각 water[r][c] = shark의 idx
    next_sharks = [[Shark() for tmp_c in range(C+1)] for tmp_r in range(R+1)]

    # 상어 이동하기
    for i in range(1, R+1):
        for j in range(1, C+1):
            if cur_sharks[i][j].size == 0:
                continue
        
            nr, nc = i, j
            # !!! 클래스 멤버 변수를 메소드의 매개변수로 넘기면 그냥 변수를 넘기는 것과 달리 차마조가 되므로 변수로 풀어주었다 !!!
            dir, speed = cur_sharks[i][j].direction, cur_sharks[i][j].speed

            # 위 / 아래 방향인 경우
            if dir == 1 or dir == 2:
                nr, nd = check_limit_y(i, dir, speed)
            # 오른쪽 / 왼쪽 방향인 경우
            else:
                nc, nd = check_limit_x(j, dir, speed)


            if next_sharks[nr][nc].size != 0:
                if cur_sharks[i][j].size > next_sharks[nr][nc].size:
                    next_sharks[nr][nc] =Shark(cur_sharks[i][j].size, cur_sharks[i][j].speed, nd)
            else:
                next_sharks[nr][nc] = Shark(cur_sharks[i][j].size, cur_sharks[i][j].speed, nd)
                

    for i in range(1, R+1):
        for j in range(1, C+1):
            cur_sharks[i][j] = Shark(next_sharks[i][j].size, next_sharks[i][j].speed, next_sharks[i][j].direction)

        

print(answer)









