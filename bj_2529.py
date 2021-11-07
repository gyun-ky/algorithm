import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

op = list(map(str, input().split()))

mem = [False] * 10
ans = []
flag = True

def max_search(step, num):
    global flag, ans, mem

    if flag == False:
        return
    
    if step == K:
        flag = False
        print(str(''.join(ans)))
        return

    if op[step] == '>':
        for new_num in range(num-1, -1, -1):
            if mem[new_num] == False:
                ans.append(str(new_num))

                mem[new_num] = True
                max_search(step+1, new_num)
                mem[new_num] = False
                ans.pop()
    else:
        for new_num in range(9, num, -1):
            if mem[new_num] == False:
                ans.append(str(new_num))
  
                mem[new_num] = True
                max_search(step+1, new_num)
                mem[new_num] = False
                ans.pop()

        
def min_search(step, num):
    global flag, ans, mem

    if flag == False:
        return
    
    if step == K:
        flag = False
        print(str(''.join(ans)))
        return

    if op[step] == '>':
        for new_num in range(0, num):
            if mem[new_num] == False:
                ans.append(str(new_num))
                mem[new_num] = True
                min_search(step+1, new_num)
                mem[new_num] = False
                ans.pop()

    else:
        for new_num in range(num+1, 10):
            if mem[new_num] == False:
                ans.append(str(new_num))
                mem[new_num] = True
                min_search(step+1, new_num)
                mem[new_num] = False
                ans.pop()


for i in range(9, -1, -1):
    if flag == True:
        ans.append(str(i))
        mem[i] = True
        max_search(0, i)
        ans.pop()
        mem[i] = False


mem = [False] * 10
ans = []
flag = True
for i in range(0, 10):
    if flag == True:
        ans.append(str(i))
        mem[i] = True
        min_search(0, i)
        ans.pop()
        mem[i] = False

