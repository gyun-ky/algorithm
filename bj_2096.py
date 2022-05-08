# N줄에 0이상 9 이하의 숫자 세개씩
# 첫줄에서 마지막 줄에서 끝나느 놀이

# 첫줄 세개 숫자 중 한개 선택 -> 다음줄 (제약조건 : 바로 아래로 넘어가기 혹은 바로 아래수와 붙어있는 수로)
# 얻을 수 있느 최대 점수, 최소 점수

N = int(input())

# data = []
# for i in range(N):
#     data.append(list(map(int, input().split())))

# 시간 복잡도
# N - 100,000
# 3 ^ 100,000 -> 최대, 최소를 구해야 하는데, 완전탐색 불가!!! 시간 초과난다

# 이게 결국 3 * 100,000를 방문하는 방법을 찾는 것이다!!

# 그리디가 아닌가
# 작은것을 선택 -> 그다음에도 작은 것을 선택 
# 그런데 이것은 현재, 123,921인 경우 3으로 가서 81을 선택하는것보다 1로가서 9를 선택하는게 좋으므로 -> 그리디 불가

# 투포인터로 푼다?????
# 투포인터의 대상을 쌓여가는 크기라고 하고 그것들을 1차원 배열을 대상으로 보자!!!
# 최대 9이하니까 900,001 크기의 배열 


# 1KB = 1000 = 1024byte
# 1MB = 1000,000 = 1024KB
# int = 4byte = 2^2
# 2^20 / 2^2 = 2^18
# 1000,000 * 4 / 4 = 1000,000 개의 숫자!!!

max_num = 0
min_num = int(1e9)

# dp1[i][j] : i,j까지 왔을 때의 최소
# dp1[i][j] = 
## j가 0인 경우 : min(dp[i-1][0] + data[i][j], dp[i-1][1] + data[i][j])
## j가 1인 경우 : min(dp[i-1][0] + data[i][j], dp[i-1][1] + data[i][j], dp[i-1][2] + data[i][j])
## j가 2인 경우 : min(dp[i-1][1] + data[i][j], dp[i-1][2] + data[i][j])

# dp1 = [[int(1e9)] * 3 for _ in range(N)]
# dp2 = [[-1]*3 for _ in range(N)]

tmp = list(map(int, input().split()))
dp1 = tmp[:]
dp2 = tmp[:]


for i in range(1,N):

    data = list(map(int, input().split()))

    candi_min_0 = [dp1[0]+data[0], dp1[1]+data[0]]
    candi_min_1 = [dp1[0]+data[1], dp1[1]+data[1], dp1[2]+data[1]]
    candi_min_2 = [dp1[1]+data[2], dp1[2]+data[2]]
    dp1 = [min(candi_min_0), min(candi_min_1), min(candi_min_2)]

    candi_max_0 = [dp2[0]+data[0], dp2[1]+data[0]]
    candi_max_1 = [dp2[0]+data[1], dp2[1]+data[1], dp2[2]+data[1]]
    candi_max_2 = [dp2[1]+data[2], dp2[2]+data[2]]
    dp2 = [max(candi_max_0), max(candi_max_1), max(candi_max_2)]


print(max(dp2), end=' ')
print(min(dp1), end=' ')

# 3*100,000 = 300,000 / 300,000 * 4 * 3 -> 3600,000
# 4000,000


# for i in range(1,N):


#     for j in range(3):
#         if j == 0:
#             tmp1 = [dp1[i][j], dp1[i-1][0] + data[i][j], dp1[i-1][1] + data[i][j]]
#             tmp2 = [dp2[i][j], dp2[i-1][0] + data[i][j], dp2[i-1][1] + data[i][j]]
            
#         elif j == 1:
#             tmp1 = [dp1[i][j], dp1[i-1][0] + data[i][j], dp1[i-1][1] + data[i][j], dp1[i-1][2] + data[i][j]]
#             tmp2 = [dp2[i][j], dp2[i-1][0] + data[i][j], dp2[i-1][1] + data[i][j], dp2[i-1][2] + data[i][j]]
    
#         else:
#             tmp1 = [dp1[i][j], dp1[i-1][1] + data[i][j], dp1[i-1][2] + data[i][j]]
#             tmp2 = [dp2[i][j], dp2[i-1][1] + data[i][j], dp2[i-1][2] + data[i][j]]
    
#         dp1[i][j] = min(tmp1)
#         dp2[i][j] = max(tmp2)

# print(max(dp2[N-1]), end=' ')
# print(min(dp1[N-1]), end=' ')



# dp2[i][j] : i,j까지 왔을 떄의 최대


