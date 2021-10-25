import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

# 0 - +, 1 - -, 3 - *, 4 - /
op_cnt = list(map(int, input().split()))
# op_start = []
# for i in range(4):
#     if op_cnt[i] != 0:
#         op_start.append(i)

# print(op_start)

max = -int(1e9)-1
min = int(1e9)


def search(idx, result, add, sub, mul, div):
    global max, min

    if idx == N:
        if max < result :
            max = result
        if min > result :
            min = result
        
        return

    if add > 0:
        search(idx+1, result+data[idx], add-1, sub, mul, div)
    if sub > 0:
        search(idx+1, result-data[idx], add, sub-1, mul, div)
    if mul > 0:
        search(idx+1, result*data[idx], add, sub, mul-1, div)
    if div > 0:
        if result//data[idx]<0:
            search(idx+1, -((-result)//data[idx]), add, sub, mul, div-1)
        else:
            search(idx+1, result//data[idx], add, sub, mul, div-1)


search(1, data[0], op_cnt[0], op_cnt[1], op_cnt[2], op_cnt[3])
print(max)
print(min)
