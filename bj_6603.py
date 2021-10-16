import sys
input = sys.stdin.readline


output = []

def DFS(arr, output, idx, depth, limit):
    if depth == 6:
        output.append(arr[idx])
        for i in output:
            print(i, end=' ')
        print()
        output.pop()
        return
    else:
        if idx <= limit:
            output.append(arr[idx])
            for i in range(idx+1, limit+1):
                DFS(arr, output, i, depth+1, limit)
            output.pop()
            return
        else:
            return
            
        


while True:
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break
    k = input_data[0]

    # 현재 노드보다 무조건 커야함
    for i in range(1, k+1):
        DFS(input_data, output, i, 1, k)
        output.clear()
    
    print()

    
                


        

