import sys
import copy
input = sys.stdin.readline

N = int(input())

plus_mem = [False] * 100
minus_mem = [False] * 100
col_mem = [False] * N


def search(row, cnt):
    
    if row == N:
        cnt += 1
        return cnt

    for col in range(0, N):
        if col_mem[col] == False and plus_mem[col+row] == False and minus_mem[row-col+N-1] == False:
            
            col_mem[col] = True
            plus_mem[row+col] = True
            minus_mem[row-col+N-1] = True

            cnt = search(row+1, cnt)

            plus_mem[row+col] = False
            minus_mem[row-col+N-1] = False
            col_mem[col] = False

    return cnt


print(search(0, 0))
