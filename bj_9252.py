in1 = list(input().strip())
in2 = list(input().strip())


in1.insert(0, '0')
in2.insert(0, '0')


dp = [[0]*1001 for i in range(1001)]

ans = ''


for i in range(1, len(in1)):
    for j in range(1, len(in2)):
        if in1[i] == in2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(in1)-1][len(in2)-1])

i = len(in1)-1
j = len(in2)-1

while True:

    if i == 0 or j == 0:
        break
    
    if in1[i] == in2[j]:
        ans = in1[i] + ans
        i = i-1
        j = j-1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i = i-1
        else:
            j = j-1
#
print(ans)
