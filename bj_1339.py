import sys
input = sys.stdin.readline

N = int(input())

alpha_score=dict()

for i in range(26):
    alpha = chr(ord('A') + i)
    alpha_score[alpha] = 0


data =[]

score = [1]
for i in range(1, 8):
    score.append(score[i-1]*10)



max_len = 0
for i in range(N):
    data.append(list(map(str, input().strip())))
    data[i].reverse()
    for j in range(0, len(data[i])):
        alpha_score[data[i][j]] += score[j]


sorted_alpha_score = sorted(alpha_score.items(), key=lambda x : x[1], reverse=True, )
        

sum = 0
for i in range(0, 9):
    sum += sorted_alpha_score[i][1]*(9-i)

print(sum)

        


