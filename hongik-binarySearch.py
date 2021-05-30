n = int(input())
numbers = list(map(int, input().split()))
sNum = int(input())

numbers.sort()

print(numbers)

def binarySearch(sIndex, eIndex, sNum):
    if(sIndex > eIndex):
        return

    mid = int((sIndex+eIndex)/2)
    if numbers[mid] == sNum:
        print(f'{sNum}은 {mid} 위치에!')
        return
    elif sNum > numbers[mid]:
        binarySearch(mid+1, eIndex, sNum)
    else:
        binarySearch(sIndex, mid-1, sNum)

binarySearch(0, n-1, sNum)
