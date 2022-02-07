from collections import deque
from re import T

s, t = map(int, input().split())


if s == t:
    print(0)

else:

    q = deque()
    visited = set()
    q.append((s, ''))


    while q:
        num, op_str = q.popleft()
        if num == t:
            print(op_str)
            exit(0)

        if 0<= num*num <= 10**9 and (num*num not in visited):
            visited.add(num*num)
            q.append((num*num, op_str+'*'))

        if 0<= num*2 <= 10**9 and (num*2 not in visited):
            visited.add(num*2)
            q.append((num*2, op_str+'+'))

        if 0 not in visited:
            visited.add(0)
            q.append((0, op_str+'-'))
    
        if num != 0 and (1 not in visited):
            visited.add(1)
            q.append((1, op_str+'/'))

    print(-1)
    


        