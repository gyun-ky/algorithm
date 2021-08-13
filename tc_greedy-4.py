import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
while N >= K :
    while N % K == 0:
        cnt+=1
        N /= K
    N -= 1
    cnt+=1

if N!=1:
    cnt += N-1

print(cnt)