
N, x = map(int, input().split())

data = list(map(int, input().split()))

cnt = 0

def binary_search(s, e, t):
    global cnt

    if s > e:
        return
    
    mid = (s+e)//2

    if data[mid] < t:
        if mid+1 <= e:
            binary_search(mid + 1, e, t)
    elif data[mid] > t:
        if mid-1 >= s:
            binary_search(s, mid-1, t)
    else:
        cnt += 1
        if mid+1 <= e:
            binary_search(mid+1, e, t)
        if mid-1 >= s:
            binary_search(s, mid-1, t)

binary_search(0, len(data)-1, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)
