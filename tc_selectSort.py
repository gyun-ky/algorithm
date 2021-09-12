import sys
input = sys.stdin.readline
INF = int(1e9)

arr = [4, 2, 6, 1, 9, 23, 45, 21, 28, 19]

def selectSort(arr):
    
    for i in range(0, len(arr)-1):
        min_val = INF
        min_idx = -1
        for j in range(i, len(arr)):
            if min_val > arr[j]:
                min_val = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selectSort(arr)
print(arr)
