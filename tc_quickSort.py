import sys
input = sys.stdin.readline

arr = [4, 2, 6, 1, 9, 23, 45, 21, 28, 19]

def quickSort(start, end, arr):
    if start>=end :
        return
    pivot = start
    left = start+1
    right = end
    while True:
        while arr[left] <= arr[pivot] and left <= end:
            left+=1
        while arr[right] >= arr[pivot] and right > pivot:
            right-=1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
            quickSort(0, right-1, arr)
            quickSort(right+1, end, arr)
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]


quickSort(0, len(arr)-1, arr)
print(arr)

