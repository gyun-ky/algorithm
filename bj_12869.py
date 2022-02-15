# 수빈 뮤탈 1개 강호 SCV N개
# SCV는 각각의 체력

# 뮤탈 한번에 세개 SCV 공격 9 -> 3 -> 1
# 한번의 공격에서 같은 SCV 여러번 공격 불가

# 모든 SCV 파괴하기 위한 공격 횟수 최솟값
from cgitb import scanvars
from itertools import permutations



N = int(input())

attack = []
for i in range(N):
    attack.append(i)


hp = list(map(int, input().split()))
print(hp)

perm = list(permutations(attack, N))
print(perm)

# dp는 SCV의 체력이 i 일 떄, 최소 횟수

# 1회 진행했을 때, 남아있는 hp?

# 배열에다가 각각의 체력일 때, 1, 2, 3 공격을 적용 했을 때를 모두 구한다
#    0, 1, 2, 4, 5, ... hp
# 0
# 1
# 2
scv_dp_hp = []
minus_hp = [9, 3, 1]
for i in range(N):
    dp = []
    for k in range(3):
        row = []
        for j in range(hp[i]+1):
            if j-minus_hp[k] <= 0:
                row.append(0)
            else:
                row.append(j-minus_hp[k])
        dp.append(row)
    # dp = [[j-minus_hp[k] for j in range(hp[i])] for k in range(3)]
    print(dp)
    scv_dp_hp.append(dp)

print(scv_dp_hp[0][2][4])


# 이런 배열이 3개
# hp 부터 시작해서 각 경우 일때의  최소 hp로 시작 그 수를 센다.
cnt = 0
tot_hp = sum(hp)
print(tot_hp)
print("-------")
while tot_hp:
    fix_perm = []
    for p in perm:
        n_tot_hp = 0

        for scv_idx in range(N):
            n_tot_hp += scv_dp_hp[scv_idx][p[scv_idx]][hp[scv_idx]]
            

        if tot_hp > n_tot_hp :
            fix_perm = p

    
    for scv_idx in range(N):
        n_tot_hp += scv_dp_hp[scv_idx][fix_perm[scv_idx]][hp[scv_idx]]
        hp[scv_idx] = scv_dp_hp[scv_idx][fix_perm[scv_idx]][hp[scv_idx]]

    tot_hp = n_tot_hp
    
    
    print(hp)
    
    cnt += 1
    
# 전체가 작으면 최소라고 생각했는데 아닌가 보다....! 다시 생각...!

print(cnt)



