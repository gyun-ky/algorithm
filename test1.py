import heapq
from re import A

q = []
heapq.heappush(q, 3)
heapq.heappush(q, 1)
heapq.heappush(q, 10)
heapq.heappush(q, 4)
print(q)

print(q[0:-1])

adict = {}

adict[1] = 1
print(adict)

adict[1] += 1
print(adict)

if 1 in adict:
    print("t")

a = "hello"
a_l = list(a.strip())
print(a_l)
b_l = a_l
b_l[0]='v'
print(b_l)
print(a_l)



a = "abc"
print(a[3:])

a = [1, 1, 3, 4]
print(set(a))