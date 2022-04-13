
n = int(input())

data = []
for i in range(n):
    data.append(list(map(str, input().split())))
    data[i][1] = int(data[i][1])
    data[i][2] = int(data[i][2])
    data[i][3] = int(data[i][3])


data.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])

