# 두 수열 주어졌을 때, 모두의 부분 수열이 되는 수열중 가장 긴것!!!

# dp[N] - N 번째까지 살펴봤을 때, 가장 긴 수열의 길이

# dp[N] = max(dp[N-1] + 만약 매치가 된다면 1 , dp[N])


in1 = list(input().strip())
in2 = list(input().strip())

# arr1 = ['0'] + in1
# arr2 = ['0'] + in2


# if len(arr1) > len(arr2):
#     long_arr = arr1
#     short_arr = arr2

# else:
#     long_arr = arr2
#     short_arr = arr1


# dp = [0]*len(short_arr)

# start = 1

# for i in range(1, len(short_arr)):
#     detect_flag = False
#     if start > len(long_arr)-1:
#         dp[i] = dp[i-1]
#         continue

#     for j in range(start, len(long_arr)):
#         if short_arr[i] == long_arr[j] :
#             dp[i] = dp[i-1] + 1
#             detect_flag = True
#             start = j+1
#             print(short_arr[i])
#             break

#     if detect_flag == False:
#         dp[i] = dp[i-1]


# print(dp[len(short_arr)-1])


# AC 로 시작할 수도 CA로 시작할 수도


# DP[i][j] i번쨰에서 j번째까지의 가장 LCS의 길이
# dp[i][j] = max(dp[i][k] + dp[k+1][j]) i = k ~ j-1

# 초기값 문제
# dp[i][i] = 

# dp[i][j] = 첫번째 i까지 왔을 때, 두번째 수열 j까지 왔을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것.
# dp[i][j] = dp[i-1][j-1] 



in1.insert(0, '0')
in2.insert(0, '0')

dp = [[0]*1001 for i in range(1001)]

for i in range(1, len(in1)):
    for j in range(1, len(in2)):
        if in1[i] == in2[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[len(in1)-1][len(in2)-1])




