# Matrix의 개수
n = int(input())

# Matrix 1번 부터 n번까지 행과열 (총 n+1개)
d = list(map(int, input().split()))

# M[i][j] : Matrix i번 부터 j번까지의 행렬을 곱하는데 필요한 원소 단위 곱셈의 최소 횟수
M = [[0 for i in range(0, n+1)] for j in range(0, n+1)]
# M[same][same] 은 어차피 연산이 없으므로 0

# Matrix i번 부터 j번까지 행렬 곱할 시 둘로 나누어졌을 때, 최소가 되는 부분
P = [[0 for i in range(0, n+1)] for j in range(0, n+1)]


# M의 대각선 방향으로 DP 계산 진행
# diag - 중간 가로지르는 대각선에서 얼마나 올라와 있는가를 나타냄
for diag in range(1, n):
    # i - 시작 matrix 즉 M에서의 행 - 전체 개수가 6개라면 대각선이 1칸 올라와 있다면 6-1 = 5까지만 본다
    for i in range(1, n-diag+1):
        # 열은 i에 비해 diag 만큼 더 가 있다
        j = i + diag
        min = M[i][i] + M[i+1][j] + d[i-1]*d[i]*d[j]
        P[i][j] = i
        for k in range(i+1, j):
            new = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
            if min > new:
                min = new
                # 단위 연산이 수가 최소가 될 떄, 파티션을 나누는 k값을 P에 넣는다 -> 추후 최적의 순서 찾아가기 위해
                P[i][j] = k
        M[i][j] = min

print(M[1][n])
print(P)


def order(i, j):
    if i == j:
        print(f'A{i}', end="")
        return
    else:
        print("(", end="")
        order(i, P[i][j])
        order(P[i][j]+1, j)
        print(")", end="")
    

order(1,6)