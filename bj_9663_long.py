import sys
import copy
input = sys.stdin.readline

N = int(input())

cnt = 0

def search(row, col_mem, plus_mem, minus_mem):
    global cnt
    
    if row == N:
        cnt += 1
        return

    for col in range(0, N):
        if col_mem[col] == False:
            if (row + col) in plus_mem:
                continue
            if (col-row) in minus_mem:
                continue
            n_col_mem = copy.deepcopy(col_mem)
            n_col_mem[col] = True
            n_plus_mem = copy.deepcopy(plus_mem)
            n_plus_mem.append(row+col)
            n_minus_mem = copy.deepcopy(minus_mem)
            n_minus_mem.append(col-row)

            search(row+1, n_col_mem, n_plus_mem, n_minus_mem)

col_mem = [False] * N
plus_mem = []
minus_mem = []

search(0, col_mem, plus_mem, minus_mem)
print(cnt)