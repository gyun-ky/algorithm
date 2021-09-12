import sys
input = sys.stdin.readline

arr = [4, 2, 6, 1, 9, 23, 45, 21, 28, 19]

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
        

insertionSort(arr)
print(arr)