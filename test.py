score = [20, 70, 40, 85, 60]
sum = 0
max_score = 0
for i in score:
    sum += i
    if max_score < i:
        max_score = i

avg = sum / len(score)

pass_fail = []

print("점수평균: {:.2f}".format(avg))
print(f'최고점수: {max_score}')
print("Pass/Fail: [", end="")

for i in range(0, len(score)):
    if i == len(score)-1:
        if score[i]>= avg:
            print("Pass]")
        else:
            print("Fail]")
    else:
        if score[i]>= avg:
            print("Pass,", end=' ')
        else:
            print("Fail,", end=' ')


