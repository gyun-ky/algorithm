import sys
input = sys.stdin.readline

N = int(input())
products = list(map(int, input().rstrip().split()))


M = int(input())
search = list(map(int, input().rstrip().split()))

products.sort()

def binary_search(products, l, h, target):
    if l>h:
        return "no"
    mid = (l+h)//2
    if products[mid] == target:
        return "yes"
    elif products[mid] < target:
        return binary_search(products, mid+1, h, target)
    else:
        return binary_search(products, l, mid-1, target)

for s in search:
    print(binary_search(products, 0, len(products), s), end=' ')

    
    
