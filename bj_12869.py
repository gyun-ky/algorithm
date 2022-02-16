from itertools import permutations

N = int(input())

attack = [-9, -3, -1]

hp = list(map(int, input().split()))

# 공격 가능한 순열 리스트
perm = list(permutations(attack, 3))

dp = [[[-1 for k in range(61)] for j in range(61)] for i in range(61)]

def dp_cal(i, j, k):
    if i<=0 and j<=0 and k<=0 :
        return 0


    if i<0:
        ni = 0
    else:
        ni = i
    if j<0:
        nj = 0
    else: 
        nj = j
    if k<0:
        nk = 0
    else: 
        nk = k

    if dp[ni][nj][nk] != -1:
        return dp[ni][nj][nk]

    min_num = int(1e9)
    for p in perm:
        result = dp_cal(ni+p[0], nj+p[1], nk+p[2]) + 1
        if result < min_num:
            min_num = result
    
    dp[ni][nj][nk] = min_num
    return min_num

if N==1:
    print(dp_cal(hp[0], 0, 0))
elif N==2:
    print(dp_cal(hp[0], hp[1], 0))
else:
    print(dp_cal(hp[0], hp[1], hp[2]))




