import sys
input = sys.stdin.readline

array = [1,3, 2, 4, 5, 2, 10, 43, 26]

array.sort()
print(array)

def binary_search(array, l, h, num):
    if l>h:
        return None
    mid = (l+h)//2
    if array[mid] == num:
        return mid
    if num > array[mid]:
        return binary_search(array, mid+1, h, num)
    else:
        return binary_search(array, l, mid-1, num)


# def binary_search(array, l, h, num):
#     start = l
#     end = h
#     while start<=end:
#         mid = (start + end) //2
#         if array[mid] == num:
#             return mid
#         if num > array[mid]:
#             start = mid+1
#         else:
#             end = mid-1
#     return None

print(binary_search(array, 0, len(array), 43))
