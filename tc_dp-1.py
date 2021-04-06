# 이것이 코딩 테스트다 다이나미 프로그래밍 실전 - 1


dp = [0] * 30001 #dp 테이블 초기화

# Top-Down 방식

# def make_one(num):
#     if num == 0 or num == 1:
#         return 0
  
#     if dp[num]!= 0:
#         return dp[num]
    
#     dp[num] = make_one(num-1) + 1
    
#     if num%5 == 0:
#         result = make_one(int(num/5)) + 1
#         if result < dp[num]:
#             dp[num] = result
    
#     if num%3 == 0:
#         result = make_one(int(num/3)) + 1
#         if result < dp[num]:
#             dp[num] = result
        

#     if num%2 == 0:
#         result = make_one(int(num/2)) + 1
#         if result < dp[num]:
#             dp[num] = result

    
#     return dp[num]

input_num = int(input())

for i in range(2, input_num+1):
    
    dp[i] = dp[i-1]+1

    if i % 5 == 0:
        dp[i] = min(dp[int(i/5)]+1, dp[i])
    
    if i % 2 == 0:
        dp[i] = min(dp[int(i/2)]+1, dp[i]) # dp[i//2]으로 해서 소수점을 없애줄 수 있다
    
    if i % 3 == 0 :
        dp[i] = min(dp[int(i/3)]+1, dp[i])

print(dp[input_num])
