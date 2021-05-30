n = int(input())
numbers = list(map(int, input().split()))


tmp = list(0 for i in range(0, n))


def merge(low, mid, high):

    i = low
    j = mid+1
    k = low
    while i<=mid and j<=high:
        if numbers[i]<=numbers[j]:
            tmp[k] = numbers[i]
            i+=1
            k+=1
        else:
            tmp[k] = numbers[j]
            j+=1
            k+=1
    if i>mid and j<=high:
        while(k<=high):
            tmp[k] = numbers[j]
            k+=1
            j+=1
    elif j>high and i<=mid:
        while(k<=high):
            tmp[k] = numbers[i]
            k+=1
            i+=1

    for l in range(low, high+1):
        numbers[l] = tmp[l]

def mergeSort(low, high):
    if low>=high:
        return
    
    m = int((low+high)/2)

    mergeSort(low, m)
    mergeSort(m+1, high)
    merge(low, m, high)

mergeSort(0, n-1)
print(numbers)

