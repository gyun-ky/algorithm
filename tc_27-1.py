


N, x = map(int, input().split())

data = list(map(int, input().split()))

def find_first_idx(s, e, t):
    
    if s > e:
        return -1
    
    m = (s+e)//2

    if data[m] == t:
        if m-1 >= 0 and data[m-1] != t:
            return m
    
    if data[m] >= t:
        if m+1 <= e:
            return find_first_idx(s, m-1, t)
    else:
        if m-1 >= 0:
            return find_first_idx(m+1, e, t)
    
def find_last_idx(s, e, t):

    if s > e:
        return -1

    m = (s+e)//2

    if data[m] == t:
        if m+1 <= e and data[m+1]!= t:
            return m
    
    if data[m] <= t:
        if m+1 <= e:
            return find_last_idx(m+1, e, t)
    else:
        if m-1 >= 0:
            return find_last_idx(s, m-1, t)


a = find_first_idx(0, len(data)-1, x)
b = find_last_idx(0, len(data)-1, x)

if a == -1 or b == -1:
    print(-1)
else:
    print(b-a+1)