import sys
input = sys.stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

answer = 0


####방법 1####

# def dfs(idx, sum, answer):
#     sum += data[idx]
#     if sum == S: 
#         answer += 1

#     if idx == N-1:
#         return answer
    
#     for i in range(idx+1, N):
#         answer = dfs(i, sum, answer)
#     return answer
    
        

# for i in range(0, N):
#     sum = data[i]
#     if sum == S :
#         answer+=1
#     if i != N-1:
#         for j in range(i+1, N):
#             answer = dfs(j, sum, answer)


###방법 2####
def search(idx, sum):
    global answer
    if idx == N:
        if sum == S : 
            answer += 1
        return
    
    search(idx+1, sum+data[idx])
    search(idx+1, sum)

search(0, 0)

# S == 0인 경우 
if S == 0:
    answer -= 1

print(answer)