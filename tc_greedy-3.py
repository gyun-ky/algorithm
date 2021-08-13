import sys
input = sys.stdin.readline
INF = 1e9

row, col = map(int, input().split())

result = 0
for i in range(0, row):
    input_list = list(map(int, input().split()))
    min_num = min(input_list)
    result = max(result, min_num)

print(result)


