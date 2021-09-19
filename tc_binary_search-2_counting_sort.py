import sys
input = sys.stdin.readline

count = [0] * 1000000

N = int(input())
for i in input().rstrip().split():
    count[i] = 1

M = int(input())
search = list(map(int, input().rstrip().split()))

for s in search:
    if count[s] == 1 :
        print("yes", end=' ')
    else :
        print("no", end =' ')