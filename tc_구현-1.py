import sys
input = sys.stdin.readline

N = int(input())

plan = list(map(str, input().split()))

print(plan)
# U D R L
move = {
    'U' : 0,
    'D' : 1,
    'R' : 2,
    'L' : 3
}
x = [-1, 1, 0, 0]
y = [0, 0, 1, -1]

i = 0
cx, cy = 1, 1
while i<len(plan):

    tmpx =  cx + x[move[plan[i]]]
    tmpy = cy + y[move[plan[i]]]
    i+=1

    if tmpx < 1 or tmpx > N or tmpy < 1 or tmpy > N:
        continue

    cx = tmpx
    cy = tmpy

    

print(f'{cx} {cy}')